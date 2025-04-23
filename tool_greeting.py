from mcp.server.fastmcp import FastMCP, Context

# MCP server
mcp = FastMCP(name="tool_greeting", host="127.0.0.1", port=5000, timeout=30)
 
 
# Simple echo tool
@mcp.tool()
def echo(message: str) -> str:
    return message + " has been input. hello world!"
 
 
# Add a tool that uses a resource
@mcp.tool()
async def greeting(name: str, ctx: Context) -> str:
    """
    Get a greeting using the greeting resource
    """
    try:
        # Method 1: Directly call the resource function
        # greeting_text = get_greeting(name)
        # return f"Tool response: {greeting_text}"

        # Method 2: Safely use read_resource
        result = await ctx.read_resource(f"greeting://{name}")
        content = result[0] if isinstance(result, tuple) else result
        return f"Tool response: {content}"
    except Exception as e:
        return f"Error retrieving greeting: {str(e)}"
 
 
# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    Get a personalized greeting
    """
    return f"Hello, {name}!! Welcome to FastMCP!"


# Run the server
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')