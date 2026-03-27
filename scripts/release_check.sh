#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

rm -rf .venv-release-check build dist agg_brake_log.jsonl agg_brake_anonymous_export.json

python3 -m venv .venv-release-check
source .venv-release-check/bin/activate

python -m pip install --upgrade pip
python -m pip install -e .
python -m unittest discover -s tests -v
python examples/basic_usage.py
python -m pip install build
python -m build

deactivate
rm -rf .venv-release-check build dist agg_brake_log.jsonl agg_brake_anonymous_export.json

echo "RELEASE_CHECK_OK"
