# Python MCP Workshop

This workshop shows how to run a small Python MCP server and connect it to GitHub Copilot in VS Code.

The server provides two tools:

- `hello_world()` returns `Hello, world!`.
- `add_numbers(first_number: float, second_number: float)` adds two numbers together.

You do not need deep MCP knowledge for this workshop. The goal is to get the server running, connect it to Copilot, and try the tools from chat.

Tool implementations live in separate files under `src/mcp_workshop/tools/`, with their MCP title, description, and hints defined next to the function. The central inventory in `src/mcp_workshop/tools/inventory.py` collects those tools and registers them with the server.

## Local setup

You need Python 3.10 or newer. If you are using Codespaces, the devcontainer already provides a suitable Python version.

From the repository root, create a virtual environment and install the project:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .[dev]
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run the server

This workshop server supports two MCP transports:

- **stdio**: best when GitHub Copilot or MCP Inspector starts the server for you.
- **HTTP**: useful when you want a local URL such as `http://127.0.0.1:8000/`.

### Option 1: stdio mode

Stdio mode is the default:

```bash
python -m mcp_workshop.server
```

You can also use the console command:

```bash
mcp-workshop
```

MCP servers in stdio mode use standard input and output to talk to MCP clients, so the terminal will wait instead of showing an interactive prompt. Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop it.

### Option 2: HTTP mode

HTTP mode starts the server at `http://127.0.0.1:8000/`:

```bash
mcp-workshop --transport http
```

You can also use the shorter version:

```bash
mcp-workshop --http
```

Keep this terminal running while Copilot or MCP Inspector is connected.

## Connect the server to GitHub Copilot in VS Code

The included `.vscode/mcp.json` uses stdio mode, which lets VS Code start the server automatically:

```json
{
  "servers": {
    "mcp-workshop": {
      "type": "stdio",
      "command": "${workspaceFolder}/.venv/bin/python",
      "args": ["-m", "mcp_workshop.server", "--transport", "stdio"]
    }
  }
}
```

On Windows, use the virtual environment Python executable in `.venv\\Scripts\\python.exe` instead of `.venv/bin/python`.

If you prefer HTTP mode, start the server first with `mcp-workshop --http`, then use this server config instead:

```json
{
  "servers": {
    "mcp-workshop": {
      "type": "http",
      "url": "http://127.0.0.1:8000/"
    }
  }
}
```

Restart VS Code or reload the window if Copilot does not pick up the server right away.

## Run MCP Inspector

MCP Inspector lets you check that the server starts and exposes the expected tools:

```bash
npx @modelcontextprotocol/inspector .venv/bin/python -m mcp_workshop.server
```

For HTTP mode, start the server first:

```bash
mcp-workshop --http
```

Then open Inspector and connect to `http://127.0.0.1:8000/` using the streamable HTTP transport. The server allows local browser connections from Inspector, so it should not be blocked by CORS.

In the Inspector, look for the `hello_world` and `add_numbers` tools.

If Inspector shows a CORS error, stop any old `mcp-workshop --http` terminal with <kbd>Ctrl</kbd>+<kbd>C</kbd>, start it again, and make sure Inspector is connecting to `http://127.0.0.1:8000/`.

## Codespaces

If you are using Codespaces, the devcontainer should install the project dependencies and helper tools automatically. It also forwards port `8000` for HTTP mode. After the Codespace finishes setting up, you can run the server, use MCP Inspector, or connect Copilot using the same commands and MCP config above.

## Prompts to try in Copilot

After connecting the server, open Copilot Chat in VS Code and try prompts like:

- `Use the workshop MCP server to echo this sentence: Hello from MCP.`
- `Use the hello_world tool.`
- `Use the add_numbers tool to add 7 and 5.`
- `What tools are available from the mcp-workshop server?`