# server.py
from mcp.server.fastmcp import FastMCP
 
# Create an MCP server
mcp = FastMCP("Demo")
 
 
# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
 
 
# Add a dynamic good bye message resource
@mcp.resource("goodbye://{name}")
def say_goodbye(name: str) -> str:
    """Get a personalized good bye message"""
    return f"Bye, {name}!"
 

if __name__ == "__main__":
    mcp.run()