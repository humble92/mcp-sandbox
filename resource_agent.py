from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP("Demo")
 
 
@mcp.resource("Agent://state")
def get_agent_state() -> str:
    """
    Function to get the state of the AI Agent

    Returns:
        str: Current mood state of the AI Agent
    """
    return f"So blue!"
 

# Run the server
if __name__ == "__main__":
    mcp.run()