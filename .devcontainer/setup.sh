#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Creating Python virtual environment in .venv..."
python -m venv .venv

echo "Upgrading pip..."
.venv/bin/python -m pip install --upgrade pip

echo "Installing the workshop package with development dependencies..."
.venv/bin/python -m pip install -e '.[dev]'

echo "Creating a copilot command that runs gh copilot..."
sudo tee /usr/local/bin/copilot >/dev/null <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is required to run Copilot from the terminal." >&2
  exit 127
fi

if [ "$#" -eq 0 ]; then
  cat <<'USAGE'
GitHub Copilot CLI runs through gh copilot.

Try one of these commands:
  copilot suggest "how do I run the tests?"
  copilot explain "python -m pytest -q"
  gh copilot --help
USAGE
  exit 0
fi

exec gh copilot "$@"
EOF
sudo chmod +x /usr/local/bin/copilot

echo "Devcontainer setup complete."
