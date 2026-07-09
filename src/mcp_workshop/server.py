"""Beginner-friendly MCP server for the Python workshop."""

from __future__ import annotations

import argparse
from typing import Any, Literal

from mcp.server.fastmcp import FastMCP

from mcp_workshop.tools.inventory import register_tools

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
MCP_ROUTE = "/"
MCP_URL = f"http://{SERVER_HOST}:{SERVER_PORT}{MCP_ROUTE}"
LOCAL_CORS_ORIGIN_REGEX = r"https?://(localhost|127\.0\.0\.1)(:\d+)?"
MCP_SESSION_HEADER = "Mcp-Session-Id"
Transport = Literal["stdio", "http"]

# Create the MCP server that clients will connect to.
mcp = FastMCP(
    "mcp-workshop",
    host=SERVER_HOST,
    port=SERVER_PORT,
    streamable_http_path=MCP_ROUTE,
)


register_tools(mcp)


def main() -> None:
    """Run the MCP server with the selected transport."""

    args = parse_args()
    run_server(args.transport)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Read the transport option from the command line."""

    parser = argparse.ArgumentParser(description="Run the Python MCP workshop server.")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="How the MCP client connects. Use 'stdio' for clients that launch the server, or 'http' for http://127.0.0.1:8000/.",
    )
    parser.add_argument(
        "--http",
        action="store_const",
        const="http",
        dest="transport",
        help="Shortcut for --transport http.",
    )
    return parser.parse_args(argv)


def run_server(transport: Transport) -> None:
    """Start the MCP server using stdio or streamable HTTP."""

    if transport == "http":
        run_http_server()
    else:
        mcp.run(transport="stdio")


def run_http_server() -> None:
    """Start the streamable HTTP server with browser-friendly CORS enabled."""

    import uvicorn

    uvicorn.run(
        create_http_app(),
        host=SERVER_HOST,
        port=SERVER_PORT,
        log_level=mcp.settings.log_level.lower(),
    )


def create_http_app() -> Any:
    """Create the HTTP MCP app and allow local browser tools to call it."""

    from starlette.middleware.cors import CORSMiddleware

    app = mcp.streamable_http_app()
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=LOCAL_CORS_ORIGIN_REGEX,
        allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=[MCP_SESSION_HEADER],
    )
    return app


if __name__ == "__main__":
    main()
