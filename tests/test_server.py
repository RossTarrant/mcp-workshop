import asyncio

from mcp_workshop import server


def test_server_has_the_example_tools() -> None:
    tools = asyncio.run(server.mcp.list_tools())

    assert {tool.name for tool in tools} == {"hello_world", "add_numbers"}


def test_example_tools() -> None:
    assert server.hello_world() == "Hello, world!"
    assert server.add_numbers(7, 5) == 12
