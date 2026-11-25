import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load('install')
uninstaller = load('uninstall')


class UninstallTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.target = Path(temp.name)
        self.output = io.StringIO()
        self.redirect = contextlib.redirect_stdout(self.output)
        self.redirect.__enter__()
        self.addCleanup(self.redirect.__exit__, None, None, None)
        installer.install(ROOT, self.target)

    def test_preview_changes_nothing(self):
        before = {str(p): p.read_bytes() for p in self.target.rglob('*') if p.is_file()}
        uninstaller.uninstall(self.target)
        after = {str(p): p.read_bytes() for p in self.target.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_removal_preserves_project_docs_and_domain_skill(self):
        domain = self.target / '.agents/skills/custom-domain/SKILL.md'
        domain.parent.mkdir(parents=True)
        domain.write_text('project domain')
        for name in ('project-profile.md', 'AGENTS.md', '.gitignore'):
            (self.target / name).write_text('user content')
        self.assertTrue(uninstaller.uninstall(self.target, True))
        self.assertTrue(domain.exists())
        self.assertEqual((self.target / 'AGENTS.md').read_text(), 'user content')
        self.assertFalse((self.target / installer.RECORD).exists())
        self.assertFalse((self.target / uninstaller.TOOL).exists())

    def test_modified_file_keeps_record_and_can_be_retried(self):
        path = self.target / '.codex/agents/developer.toml'
        original = path.read_bytes()
        path.write_text('customized')
        self.assertFalse(uninstaller.uninstall(self.target, True))
        self.assertEqual(path.read_text(), 'customized')
        self.assertTrue((self.target / installer.RECORD).exists())
        self.assertTrue((self.target / uninstaller.TOOL).exists())
        path.write_bytes(original)
        self.assertTrue(uninstaller.uninstall(self.target, True))

    def test_unsafe_manifest_rejected_before_deleting(self):
        record_path = self.target / installer.RECORD
        record = json.loads(record_path.read_text())
        record['files']['../outside'] = '0' * 64
        record_path.write_text(json.dumps(record))
        with self.assertRaises(ValueError):
            uninstaller.uninstall(self.target, True)
        self.assertTrue((self.target / '.codex/agents/developer.toml').exists())

    def test_symlink_is_preserved(self):
        path = self.target / '.codex/agents/developer.toml'
        outside = self.target / 'user.toml'
        outside.write_text('user data')
        path.unlink()
        path.symlink_to(outside)
        self.assertFalse(uninstaller.uninstall(self.target, True))
        self.assertTrue(path.is_symlink())
        self.assertEqual(outside.read_text(), 'user data')

    def test_missing_record_refuses_deletion(self):
        (self.target / installer.RECORD).unlink()
        with self.assertRaises(ValueError):
            uninstaller.uninstall(self.target, True)
        self.assertTrue((self.target / '.codex/agents/developer.toml').exists())

    def test_installer_inventory_is_accepted_by_uninstaller(self):
        self.assertEqual(set(installer.SKILLS), uninstaller.SKILLS)
        record = json.loads((self.target / installer.RECORD).read_text())
        for name in record['files']:
            self.assertTrue(uninstaller.valid_name(name), name)
        self.assertIn('.agents/skills/systematic-debugging/SKILL.md', record['files'])
