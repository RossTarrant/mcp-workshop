"""Central inventory for all workshop tools."""

from mcp.server.fastmcp import FastMCP

from mcp_workshop.tools.definitions import ToolFunction, get_tool_definition
from mcp_workshop.tools.greetings import hello_world
from mcp_workshop.tools.math_tools import add_numbers

TOOL_INVENTORY: tuple[ToolFunction, ...] = (
    hello_world,
    add_numbers,
)


def register_tools(mcp: FastMCP) -> None:
    """Register every tool in the inventory with the MCP server."""

    for tool_function in TOOL_INVENTORY:
        definition = get_tool_definition(tool_function)
        mcp.tool(
            title=definition.title,
            description=definition.description,
            annotations=definition.annotations,
        )(definition.function)
