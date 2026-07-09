# Build your first MCP server

In this workshop you will create tools that GitHub Copilot can use. You only
need basic Python knowledge—MCP handles the connection for you.

## 1. Open the project

The easiest option is to open this repository in GitHub Codespaces. Wait for
the setup to finish, then open Copilot Chat in VS Code.

If you are working locally, install Python 3.10 or newer and run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## 2. Try the example tools

The included `.vscode/mcp.json` tells Copilot how to start the server. Reload
the VS Code window after setup, then ask Copilot:

> Use the hello_world tool.

> Use the add_numbers tool to add 7 and 5.

Copilot may ask for permission before running a tool.

## 3. Create your own tool

Open `src/mcp_workshop/server.py`. A tool is an ordinary Python function with
`@mcp.tool()` written above it:

```python
@mcp.tool()
def favourite_colour(name: str) -> str:
    """Tell someone your favourite colour."""
    return f"{name}, my favourite colour is blue!"
```

Add your function above the `Add your own tools above this line` comment.

Keep these three things in mind:

1. Give the function a clear name.
2. Add a type such as `str`, `int`, or `float` to every input.
3. Use the text inside triple quotes to explain what the tool does.

Reload the VS Code window, then ask Copilot to use your new tool.

## Test your work

Run:

```bash
pytest
```

You can also start the server yourself:

```bash
python -m mcp_workshop.server
```

The terminal will wait silently because the server is listening for an MCP
client. Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop it.

## If a tool does not appear

1. Save `server.py`.
2. Check the terminal for a Python error.
3. Reload the VS Code window.
4. Check that your function has `@mcp.tool()` directly above it.
