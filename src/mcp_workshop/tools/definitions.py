"""Small helpers for defining workshop tools with nearby MCP metadata."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, TypeVar

from mcp.types import ToolAnnotations

ToolFunction = Callable[..., Any]
ToolFunctionT = TypeVar("ToolFunctionT", bound=ToolFunction)
TOOL_DEFINITION_ATTRIBUTE = "__mcp_workshop_tool_definition__"


@dataclass(frozen=True)
class ToolDefinition:
    """A Python function plus the MCP metadata shown to clients."""

    function: ToolFunction
    title: str
    description: str
    annotations: ToolAnnotations


def workshop_tool(
    *,
    title: str,
    description: str,
    annotations: ToolAnnotations,
) -> Callable[[ToolFunctionT], ToolFunctionT]:
    """Attach MCP metadata to a tool function without registering it yet."""

    def decorator(function: ToolFunctionT) -> ToolFunctionT:
        definition = ToolDefinition(
            function=function,
            title=title,
            description=description,
            annotations=annotations,
        )
        setattr(function, TOOL_DEFINITION_ATTRIBUTE, definition)
        return function

    return decorator


def get_tool_definition(function: ToolFunction) -> ToolDefinition:
    """Read the MCP metadata attached by the workshop_tool decorator."""

    definition = getattr(function, TOOL_DEFINITION_ATTRIBUTE, None)
    if not isinstance(definition, ToolDefinition):
        raise RuntimeError(f"{function.__name__} is missing workshop tool metadata.")

    return definition
