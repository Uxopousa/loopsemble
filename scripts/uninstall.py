"""Preview or remove unchanged files recorded by the agent workflow installer."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

RECORD = '.agent-workflow-install.json'
SKILLS = {'project-setup', 'team-workflow', 'clean-code-architecture',
          'frontend-design', 'testing', 'accessibility', 'angular-guidelines', 'systematic-debugging'}
AGENTS = {'planner.toml', 'developer.toml', 'reviewer.toml',
          'test-specialist.toml', 'security-reviewer.toml'}
TOOL = '.agents/agent-workflow/uninstall.py'


def valid_name(name):
    if not isinstance(name, str) or '\\' in name or ':' in name:
        return False
    parts = PurePosixPath(name).parts
    if not parts or name != '/'.join(parts) or any(p in ('.', '..') for p in parts):
        return False
    return (name == TOOL or
            (len(parts) == 3 and parts[:2] == ('.codex', 'agents') and parts[2] in AGENTS) or
            (len(parts) >= 4 and parts[:2] == ('.agents', 'skills') and parts[2] in SKILLS))


def inspect(target, name, checksum):
    path = target / name
    for candidate in (path, *path.parents):
        if candidate == target:
            break
        if candidate.is_symlink():
            return 'preservar (enlace)'
    if not path.exists():
        return 'ausente'
    if not path.is_file():
        return 'preservar (no es archivo)'
    if hashlib.sha256(path.read_bytes()).hexdigest() != checksum:
        return 'preservar (modificado)'
    return 'retirar'


def uninstall(target, apply=False):
    if not target.is_absolute() or not target.is_dir():
        raise ValueError('El destino debe ser un directorio existente con ruta absoluta.')
    target = target.resolve()
    record_path = target / RECORD
    if record_path.is_symlink() or not record_path.is_file():
        raise ValueError('No hay un registro regular de instalación; no se retirará nada.')
    record_bytes = record_path.read_bytes()
    record = json.loads(record_bytes)
    if not isinstance(record, dict) or record.get('schema') != 1:
        raise ValueError('Formato de registro no admitido.')
    files = record.get('files')
    if not isinstance(files, dict) or not files:
        raise ValueError('Inventario vacío o inválido.')
    # Validate the whole inventory before considering any deletion.
    for name, checksum in files.items():
        if not valid_name(name) or not isinstance(checksum, str) or not re.fullmatch('[a-f0-9]{64}', checksum):
            raise ValueError(f'Entrada de registro no permitida: {name!r}')
    for name, checksum in files.items():
        print(f'{inspect(target, name, checksum)}: {name}')
    if not apply:
        print('Vista previa: no se ha cambiado nada. Usa --apply para retirar solo archivos sin cambios.')
        return False
    if record_path.read_bytes() != record_bytes:
        raise ValueError('El registro cambió durante la revisión; repite la operación.')
    parents = set()
    for name, checksum in files.items():
        if name != TOOL and inspect(target, name, checksum) == 'retirar':
            path = target / name
            path.unlink()
            parents.update(p for p in path.parents if p != target and target in p.parents)
    # Only remove empty directories that contained removed pack files.
    for directory in sorted(parents, key=lambda p: len(p.parts), reverse=True):
        if directory.is_dir() and not directory.is_symlink() and not any(directory.iterdir()):
            directory.rmdir()
    remaining = [name for name, checksum in files.items() if inspect(target, name, checksum) != 'ausente']
    protected = [name for name in remaining if name != TOOL or inspect(target, name, files[name]) != 'retirar']
    if protected:
        print('Desinstalación parcial: se conserva el registro y los archivos protegidos. Revisa y vuelve a ejecutar.')
        return False
    if record_path.read_bytes() != record_bytes:
        raise ValueError('El registro cambió; se conserva para revisión.')
    if TOOL in files and inspect(target, TOOL, files[TOOL]) == 'retirar':
        (target / TOOL).unlink()
        tool_dir = (target / TOOL).parent
        if not any(tool_dir.iterdir()):
            tool_dir.rmdir()
    record_path.unlink()
    print('Archivos del pack retirados. Se conservan documentos, skills propias y configuración del proyecto.')
    print('Revisa referencias al workflow en AGENTS.md, el perfil y reglas de Git: no se modifican automáticamente.')
    return True


def main():
    if sys.version_info < (3, 9):
        raise SystemExit('Se requiere Python 3.9 o posterior.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', type=Path, help='Raíz absoluta del proyecto')
    parser.add_argument('--apply', action='store_true', help='Retirar archivos sin modificaciones')
    args = parser.parse_args()
    try:
        complete = uninstall(args.target, args.apply)
    except (OSError, ValueError) as error:
        raise SystemExit(f'Error de desinstalación: {error}') from error
    if args.apply and not complete:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
