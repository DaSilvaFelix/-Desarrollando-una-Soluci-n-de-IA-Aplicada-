from mcp.server import FastMCP

mcp = FastMCP("chatbot-server")

# Registrar una herramienta
@mcp.tool("echo")
async def echo_tool(input: str):
	print("llamado de la tool de echo ")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")