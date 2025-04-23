from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP()
 
 
@mcp.prompt()
def prompt_decision(contents: str) -> str:
    """prompt to request separating evidence and decision in the response."""
    return f"""{contents}

Please respond to this prompt using the following format.

* Evidence:

* Decision:
"""

@mcp.prompt()
def prompt_opinion(contents: str) -> str:
    """prompt to request separating fact and opinion in the response."""
    return f"""{contents}

Please respond to this prompt using the following format.

* Fact:

* Opinion:
"""
 

if __name__ == "__main__":
    mcp.run()