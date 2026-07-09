"""Math tools for the workshop server."""

from typing import Annotated

from mcp.types import ToolAnnotations
from pydantic import Field

from mcp_workshop.tools.definitions import workshop_tool


@workshop_tool(
    title="Add two numbers",
    description="Add two numbers together and return the result.",
    annotations=ToolAnnotations(
        readOnlyHint=True,
        destructiveHint=False,
        idempotentHint=True,
    ),
)
def add_numbers(
    first_number: Annotated[float, Field(description="The first number to add.")],
    second_number: Annotated[float, Field(description="The second number to add.")],
) -> float:
    """Add two numbers together."""

    return first_number + second_number
