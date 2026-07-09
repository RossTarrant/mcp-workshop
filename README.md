# Build your first MCP server

This workshop is for beginners. You do not need to have used GitHub Copilot or
MCP before.

By the end, you will have:

- used two example tools;
- created a Python tool of your own; and
- asked Copilot to run your tool.

## What are Copilot, MCP, and tools?

- **GitHub Copilot** is an AI assistant inside VS Code. You can type requests
  into Copilot Chat.
- An **MCP server** is a small program that gives Copilot extra abilities.
- A **tool** is one of those abilities. In this project, each tool is a Python
  function.

For example, this server has an `add_numbers` tool. Copilot can choose that
tool, send it two numbers, and show you the answer.

## Part 1: Open the workshop

Use GitHub Codespaces so that everything is installed for you.

1. Open this repository on GitHub.
2. Select the green **Code** button.
3. Select the **Codespaces** tab.
4. Select **Create codespace on main**.
5. Wait until VS Code appears and the terminal says:
   `Devcontainer setup complete.`

You are now using VS Code in your browser. The files are on the left, the code
editor is in the middle, and the terminal is at the bottom.

> If GitHub asks you to sign in or enable Copilot, follow the message on screen.
> Ask your teacher if your account does not have access to Copilot.

## Part 2: Open Copilot Chat

1. Find the Copilot icon near the top of VS Code.
2. Select it to open **Copilot Chat**.
3. If asked to sign in, sign in with your GitHub account.
4. Type this into the chat box and press <kbd>Enter</kbd>:

   > Say hello in one short sentence.

If Copilot replies, it is ready.

## Part 3: Try the MCP server

This project is already configured to connect the server to Copilot.

1. Reload VS Code: open the Command Palette with
   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>, type
   `Developer: Reload Window`, and press <kbd>Enter</kbd>.
2. Open Copilot Chat again.
3. Enter:

   > Use the hello_world tool from mcp-workshop.

4. Copilot may ask for permission to use the tool. Select **Allow** or
   **Continue**.
5. You should see `Hello, world!`.
6. Now enter:

   > Use the add_numbers tool from mcp-workshop to add 7 and 5.

You should get `12`.

## Part 4: Create your own tool

Open `src/mcp_workshop/server.py` from the file list on the left.

Find the comment that says `STEP 3`. Directly above that comment, copy and
paste this tool:

```python
@mcp.tool()
def favourite_colour(name: str) -> str:
    """Tell someone your favourite colour."""
    return f"{name}, my favourite colour is blue!"
```

Change `blue` to your favourite colour, then save the file with
<kbd>Ctrl</kbd>+<kbd>S</kbd>.

What each line means:

- `@mcp.tool()` tells the server that Copilot is allowed to use the function.
- `def favourite_colour...` gives the tool a name and one input called `name`.
- `str` means the input and answer are text.
- The text inside `"""` explains the tool to Copilot.
- `return` gives the answer back to Copilot.

## Part 5: Use your tool

1. Reload VS Code again using `Developer: Reload Window`.
2. Open Copilot Chat.
3. Enter:

   > Use the favourite_colour tool from mcp-workshop. My name is Alex.

4. Allow the tool if Copilot asks for permission.

You have built and used your first MCP tool.

## Create a tool of your own

Choose something small and fun. For example, your tool could:

- create a superhero name;
- convert minutes to seconds;
- recommend a film genre;
- calculate the area of a rectangle; or
- give a random study suggestion.

Use this template:

```python
@mcp.tool()
def your_tool_name(your_input: str) -> str:
    """Explain clearly what your tool does."""
    return "Replace this with your answer"
```

Change the function name, input, explanation, and returned answer. Save the
file, reload VS Code, and ask Copilot to use the new tool.

## If something does not work

Try these checks in order:

1. **Copilot does not open:** make sure you are signed in to GitHub and ask
   your teacher to check that you have Copilot access.
2. **Your tool does not appear:** save `server.py`, then reload VS Code.
3. **Copilot does not use the tool:** ask it to
   `Use the TOOL_NAME tool from mcp-workshop`.
4. **There is a red line in your code:** compare your tool with the template.
   Check the brackets, colon, quotation marks, and indentation.
5. **The server reports an error:** undo your latest change with
   <kbd>Ctrl</kbd>+<kbd>Z</kbd>, save, and reload VS Code.
6. **It still does not work:** show your code and the complete error message to
   your teacher.

## Optional: run the tests

In the terminal at the bottom of VS Code, enter:

```bash
pytest
```

The result should say `2 passed`.

## Optional: work without Codespaces

Install Python 3.10 or newer, open a terminal in this repository, and run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

On Windows PowerShell, replace the second command with:

```powershell
.venv\Scripts\Activate.ps1
```
