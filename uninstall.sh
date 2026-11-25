#!/usr/bin/env bash
set -euo pipefail
bundle_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
if ! command -v python3 >/dev/null 2>&1; then
  printf 'Se requiere Python 3.9 o posterior.\n' >&2
  exit 2
fi
exec python3 "$bundle_dir/scripts/uninstall.py" "$@"
