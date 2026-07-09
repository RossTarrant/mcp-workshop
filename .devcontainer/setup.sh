#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Creating Python virtual environment in .venv..."
python -m venv .venv

echo "Upgrading pip..."
.venv/bin/python -m pip install --upgrade pip

echo "Installing the workshop package with development dependencies..."
.venv/bin/python -m pip install -e '.[dev]'

echo "Checking for GitHub Copilot CLI support in gh..."
if command -v gh >/dev/null 2>&1; then
  if gh extension list | grep -q 'github/gh-copilot'; then
    echo "GitHub Copilot CLI extension for gh is already installed."
  elif gh extension install github/gh-copilot; then
    echo "Installed GitHub Copilot CLI extension for gh."
  else
    echo "Could not install the GitHub Copilot CLI extension for gh."
    echo "This can happen when GitHub authentication is not available during setup."
    echo "Container creation will continue. To install it later, run:"
    echo "  gh extension install github/gh-copilot"
  fi
else
  echo "GitHub CLI was not found, so gh copilot setup was skipped."
fi

echo "Creating a copilot command that runs gh copilot..."
sudo tee /usr/local/bin/copilot >/dev/null <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI is required to run Copilot from the terminal." >&2
  exit 127
fi

exec gh copilot "$@"
EOF
sudo chmod +x /usr/local/bin/copilot

echo "Devcontainer setup complete."
