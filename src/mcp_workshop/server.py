"""A small MCP server for the workshop."""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("mcp-workshop")


@mcp.tool()
def hello_world() -> str:
    """Return a friendly hello message."""
    return "Hello, world!"


@mcp.tool()
def add_numbers(first_number: float, second_number: float) -> float:
    """Add two numbers together."""
    return first_number + second_number


# Add your own tools above this line.


def main() -> None:
    """Start the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
