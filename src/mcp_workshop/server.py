"""The MCP server you will add your own tools to."""

# FastMCP does the complicated MCP work for us.
from mcp.server.fastmcp import FastMCP


# This creates the server and gives it the name shown in Copilot.
mcp = FastMCP("mcp-workshop")


# STEP 1: @mcp.tool() makes the Python function available to Copilot.
@mcp.tool()
def hello_world() -> str:
    # This explanation helps Copilot decide when to use the tool.
    """Return a friendly hello message."""

    # return sends the tool's answer back to Copilot.
    return "Hello, world!"


# STEP 2: Tools can receive information. This one receives two numbers.
@mcp.tool()
def add_numbers(first_number: float, second_number: float) -> float:
    """Add two numbers together."""
    return first_number + second_number


# STEP 3: Add your own tools above this line.


def main() -> None:
    """Start the MCP server."""

    # The server waits here for Copilot to ask it to use a tool.
    mcp.run()


# This starts the server when Python opens this file.
if __name__ == "__main__":
    main()
