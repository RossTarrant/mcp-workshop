"""Greeting tools for the workshop server."""

from mcp.types import ToolAnnotations

from mcp_workshop.tools.definitions import workshop_tool


@workshop_tool(
    title="Hello world",
    description="Return a friendly Hello, world message.",
    annotations=ToolAnnotations(
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
    ),
)
def hello_world() -> str:
    """Return a friendly Hello, world message."""

    return "Hello, world!"
