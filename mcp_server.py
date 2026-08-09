import os

from mcp.server.mcpserver import MCPServer

server = MCPServer(
    name="cookie-workspace-server",
    version="0.1.0",
    description="A minimal MCP server for the current workspace",
)


@server.tool()
def ping() -> str:
    return "pong"


@server.tool()
def workspace_status() -> str:
    return "Workspace ready"


if __name__ == "__main__":
    transport = os.environ.get("MCP_TRANSPORT", "streamable-http")
    if transport == "stdio":
        server.run(transport="stdio")
    else:
        host = os.environ.get("MCP_HOST", "127.0.0.1")
        port = int(os.environ.get("MCP_PORT", "8000"))
        server.run(transport="streamable-http", host=host, port=port)
