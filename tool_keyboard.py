# Task to control keyboard to type message in Notepad
from mcp.server.fastmcp import FastMCP
 
# MCP server
mcp = FastMCP(name="tool_keyboard", host="127.0.0.1", port=5010, timeout=30)
 
 
@mcp.tool()
def control_keyboard(message: str) -> str:
    """
    Type a message in Notepad
    """
    import pyautogui
    import time
 
    # Run Notepad
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.typewrite("notepad\n", interval=0.1)
    time.sleep(1)
 
    # Type message
    pyautogui.typewrite(message, interval=0.1)
 
    return f"'{message}' has been typed in Notepad."
 
 
# Run the server
if __name__ == "__main__":
    mcp.run()