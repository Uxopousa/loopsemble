"""Install project-scoped Codex files with an ownership record and rollback."""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
import signal
import sys

RECORD = '.agent-workflow-install.json'
SKILLS = ('project-setup', 'team-workflow', 'clean-code-architecture',
          'frontend-design', 'testing', 'accessibility', 'angular-guidelines', 'systematic-debugging')
REQUIRED = [
    *[f'.agents/skills/{name}/SKILL.md' for name in SKILLS],
    'scripts/uninstall.py',
    *[f'.codex/agents/{name}.toml' for name in
      ('planner', 'developer', 'reviewer', 'test-specialist', 'security-reviewer')],
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def install(bundle, target):
    if not target.is_absolute() or not target.is_dir():
        raise ValueError('El destino debe ser un directorio existente con ruta absoluta.')
    target = target.resolve()
    bundle = bundle.resolve()
    if target == bundle or bundle in target.parents:
        raise ValueError('El destino no puede estar dentro del paquete.')
    version = (bundle / 'VERSION').read_text().strip()
    for relative in REQUIRED:
        if not (bundle / relative).is_file():
            raise ValueError(f'Paquete incompleto: falta {relative}')
    for skill in SKILLS:
        skill_root = bundle / '.agents/skills' / skill
        if not (skill_root / 'agents/openai.yaml').is_file():
            raise ValueError(f'Faltan metadatos de la skill {skill}')
        for document in skill_root.rglob('*.md'):
            for reference in re.findall(r'`((?:references|assets)/[^`]+)`', document.read_text()):
                if not (skill_root / reference).is_file():
                    raise ValueError(f'Referencia ausente: {skill}/{reference}')
    sources = []
    roots = [bundle / '.agents/skills' / skill for skill in SKILLS]
    roots += [bundle / name for name in REQUIRED if name.startswith('.codex/agents/')]
    for root in roots:
        for candidate in (root, *root.parents):
            if candidate == bundle:
                break
            if candidate.is_symlink():
                raise ValueError(f'Enlace no permitido en el paquete: {candidate.relative_to(bundle)}')
        for path in ([root] if root.is_file() else sorted(root.rglob('*'))):
            if path.is_symlink():
                raise ValueError(f'Enlace no permitido en el paquete: {path.relative_to(bundle)}')
            if path.is_file():
                sources.append(path)
    payload = {p.relative_to(bundle).as_posix(): p.read_bytes() for p in sources}
    payload['.agents/agent-workflow/uninstall.py'] = (bundle / 'scripts/uninstall.py').read_bytes()
    record = {
        'schema': 1, 'version': version,
        'source_template': bundle.relative_to(target).as_posix() if target in bundle.parents else None,
        'files': {name: digest(data) for name, data in payload.items()},
    }
    payload = {RECORD: (json.dumps(record, indent=2) + '\n').encode(), **payload}
    for name in payload:
        destination = target / name
        if destination.exists() or destination.is_symlink():
            raise ValueError(f'Destino existente; no se ha copiado nada: {name}')
        parent = destination.parent
        while parent != target:
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise ValueError(f'Directorio no disponible: {parent.relative_to(target)}')
            parent = parent.parent
    created_files, created_dirs = [], []
    try:
        for name, data in payload.items():
            destination = target / name
            missing = []
            parent = destination.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for directory in reversed(missing):
                directory.mkdir()
                created_dirs.append(directory)
            # Exclusive creation prevents overwriting a file created after preflight.
            fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            created_files.append(destination)
            with os.fdopen(fd, 'wb') as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
        for name, data in payload.items():
            if (target / name).read_bytes() != data:
                raise ValueError(f'No se pudo verificar {name}')
    except BaseException:
        for path in reversed(created_files):
            path.unlink(missing_ok=True)
        for directory in reversed(created_dirs):
            directory.rmdir()
        raise
    print(f'Instalación {version}: {len(payload) - 1} archivos verificados en {target}')
    print('Abre una sesión nueva de Codex en esa raíz e invoca $project-setup.')
    print(f'Registro de instalación: {RECORD}')


def main():
    if sys.version_info < (3, 9):
        raise SystemExit('Se requiere Python 3.9 o posterior.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', type=Path, help='Ruta absoluta a la raíz del proyecto')
    args = parser.parse_args()
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))
    try:
        install(Path(__file__).resolve().parents[1], args.target)
    except (OSError, ValueError) as error:
        raise SystemExit(f'Error de instalación: {error}') from error


if __name__ == '__main__':
    main()
