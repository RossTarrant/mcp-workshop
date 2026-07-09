#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Creating Python virtual environment in .venv..."
python -m venv .venv

echo "Upgrading pip..."
.venv/bin/python -m pip install --upgrade pip

echo "Installing the workshop package with development dependencies..."
.venv/bin/python -m pip install -e '.[dev]'

echo "Devcontainer setup complete."
