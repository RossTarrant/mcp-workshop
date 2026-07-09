import asyncio
from unittest.mock import patch

from starlette.testclient import TestClient

from mcp_workshop import server
from mcp_workshop.tools.definitions import get_tool_definition
from mcp_workshop.tools.greetings import hello_world
from mcp_workshop.tools.inventory import TOOL_INVENTORY
from mcp_workshop.tools.math_tools import add_numbers


def test_server_registers_exactly_two_tools() -> None:
    tools = asyncio.run(server.mcp.list_tools())

    assert {tool.name for tool in tools} == {"hello_world", "add_numbers"}


def test_tools_include_titles_descriptions_and_annotations() -> None:
    registered_tools = {tool.name: tool for tool in asyncio.run(server.mcp.list_tools())}

    hello_tool = registered_tools["hello_world"]
    assert hello_tool.title == "Hello world"
    assert hello_tool.description == "Return a friendly Hello, world message."
    assert hello_tool.annotations is not None
    assert hello_tool.annotations.readOnlyHint is True
    assert hello_tool.annotations.destructiveHint is False
    assert hello_tool.annotations.idempotentHint is True
    assert hello_tool.annotations.openWorldHint is None

    add_tool = registered_tools["add_numbers"]
    assert add_tool.title == "Add two numbers"
    assert add_tool.description == "Add two numbers together and return the result."
    assert add_tool.annotations is not None
    assert add_tool.annotations.readOnlyHint is True
    assert add_tool.annotations.destructiveHint is False
    assert add_tool.annotations.idempotentHint is True
    assert add_tool.annotations.openWorldHint is None


def test_tool_inventory_collects_tools_from_source_modules() -> None:
    tool_names = {tool_function.__name__ for tool_function in TOOL_INVENTORY}

    assert tool_names == {"hello_world", "add_numbers"}
    assert get_tool_definition(hello_world).title == "Hello world"
    assert get_tool_definition(add_numbers).title == "Add two numbers"


def test_add_numbers_arguments_include_descriptions() -> None:
    registered_tools = {tool.name: tool for tool in asyncio.run(server.mcp.list_tools())}
    add_tool = registered_tools["add_numbers"]

    properties = add_tool.inputSchema["properties"]
    assert properties["first_number"]["description"] == "The first number to add."
    assert properties["second_number"]["description"] == "The second number to add."


def test_registered_tools_return_expected_values() -> None:
    async def call_tools() -> tuple[dict[str, object] | None, dict[str, object] | None]:
        _, hello_result = await server.mcp.call_tool("hello_world", {})
        _, add_result = await server.mcp.call_tool(
            "add_numbers",
            {"first_number": 1.5, "second_number": 2.25},
        )
        return hello_result, add_result

    hello_result, add_result = asyncio.run(call_tools())

    assert hello_result == {"result": "Hello, world!"}
    assert add_result == {"result": 3.75}


def test_source_tool_functions_still_work_directly() -> None:
    assert hello_world() == "Hello, world!"
    assert add_numbers(7, 5) == 12


def test_server_uses_http_transport_settings() -> None:
    assert server.MCP_URL == "http://127.0.0.1:8000/"
    assert server.mcp.settings.host == server.SERVER_HOST
    assert server.mcp.settings.port == server.SERVER_PORT
    assert server.mcp.settings.streamable_http_path == server.MCP_ROUTE


def test_command_line_defaults_to_stdio_and_supports_http() -> None:
    assert server.parse_args([]).transport == "stdio"
    assert server.parse_args(["--transport", "http"]).transport == "http"
    assert server.parse_args(["--http"]).transport == "http"


def test_run_server_maps_workshop_transports_to_mcp_transports() -> None:
    with patch.object(server.mcp, "run") as fake_run, patch.object(server, "run_http_server") as fake_http:
        server.run_server("stdio")
        server.run_server("http")

    fake_run.assert_called_once_with(transport="stdio")
    fake_http.assert_called_once_with()


def test_http_app_allows_local_inspector_cors_preflight() -> None:
    client = TestClient(server.create_http_app())

    response = client.options(
        server.MCP_ROUTE,
        headers={
            "Origin": "http://localhost:6274",
            "Access-Control-Request-Method": "POST",
        },
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:6274"
    assert "POST" in response.headers["access-control-allow-methods"]
