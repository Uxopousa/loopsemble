import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/install.py'
spec = importlib.util.spec_from_file_location('workflow_install', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.bundle = self.base / 'bundle'
        shutil.copytree(SCRIPT.parents[1], self.bundle, ignore=shutil.ignore_patterns('__pycache__'))
        self.target = self.base / 'target with spaces'
        self.target.mkdir()

    def test_install_hashes_and_no_personal_source_path(self):
        module.install(self.bundle, self.target)
        record = json.loads((self.target / module.RECORD).read_text())
        self.assertIsNone(record['source_template'])
        for name, checksum in record['files'].items():
            self.assertEqual(checksum, module.digest((self.target / name).read_bytes()))

    def test_missing_required_file_leaves_target_empty(self):
        (self.bundle / module.REQUIRED[0]).unlink()
        with self.assertRaises(ValueError):
            module.install(self.bundle, self.target)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_existing_files_are_preserved(self):
        dest = self.target / module.REQUIRED[0]
        dest.parent.mkdir(parents=True)
        dest.write_text('user changes')
        with self.assertRaises(ValueError):
            module.install(self.bundle, self.target)
        self.assertEqual(dest.read_text(), 'user changes')
        self.assertFalse((self.target / module.RECORD).exists())

    def test_failure_rolls_back_and_retry_works(self):
        original = module.os.open
        calls = 0
        def fail_midway(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 5:
                raise OSError('simulated failure')
            return original(*args, **kwargs)
        with patch.object(module.os, 'open', side_effect=fail_midway):
            with self.assertRaises(OSError):
                module.install(self.bundle, self.target)
        self.assertEqual(list(self.target.iterdir()), [])
        module.install(self.bundle, self.target)
        self.assertTrue((self.target / module.RECORD).exists())

    def test_symlink_parent_is_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        (self.target / '.agents').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            module.install(self.bundle, self.target)
        self.assertEqual(list(outside.iterdir()), [])

    def test_relative_source_is_recorded(self):
        nested = self.target / 'template'
        shutil.copytree(self.bundle, nested)
        module.install(nested, self.target)
        record = json.loads((self.target / module.RECORD).read_text())
        self.assertEqual(record['source_template'], 'template')

    def test_repeat_install_does_not_overwrite(self):
        module.install(self.bundle, self.target)
        record = (self.target / module.RECORD).read_bytes()
        with self.assertRaises(ValueError):
            module.install(self.bundle, self.target)
        self.assertEqual((self.target / module.RECORD).read_bytes(), record)

    def test_missing_workflow_reference_is_rejected(self):
        (self.bundle / '.agents/skills/team-workflow/references/testing-workflow.md').unlink()
        with self.assertRaises(ValueError):
            module.install(self.bundle, self.target)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_unrelated_bundle_configuration_is_not_installed(self):
        extra = self.bundle / '.codex/config.toml'
        extra.write_text('[agents]\nenabled = false\n')
        module.install(self.bundle, self.target)
        self.assertFalse((self.target / '.codex/config.toml').exists())
        record = json.loads((self.target / module.RECORD).read_text())
        self.assertNotIn('.codex/config.toml', record['files'])
