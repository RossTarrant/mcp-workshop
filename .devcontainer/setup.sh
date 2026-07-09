#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Creating Python virtual environment in .venv..."
python -m venv .venv

echo "Upgrading pip..."
.venv/bin/python -m pip install --upgrade pip

echo "Installing the workshop package with development dependencies..."
.venv/bin/python -m pip install -e '.[dev]'

echo "Installing GitHub Copilot CLI..."
if command -v npm >/dev/null 2>&1; then
  sudo rm -f /usr/local/bin/copilot
  sudo npm install -g @github/copilot
else
  echo "npm was not found, so GitHub Copilot CLI could not be installed."
  echo "The devcontainer includes Node.js, so rebuild the container if this happens."
fi

echo "Devcontainer setup complete."
