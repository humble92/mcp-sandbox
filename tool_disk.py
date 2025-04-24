# https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
# Feature support matrix:
# https://github.com/modelcontextprotocol/docs/diffs/0?base_sha=af2c937a7cc8e77869ea58de0534f1e5085053a8&head_user=jaw9c&name=main&pull_number=247&qualified_name=refs%2Fheads%2Fmain&sha1=af2c937a7cc8e77869ea58de0534f1e5085053a8&sha2=5ec0f72156b0585402935578d5f22c6ec14bf50a&short_path=bb2ce47&unchanged=expanded&w=false

from mcp.server.fastmcp import FastMCP

# MCP server
mcp = FastMCP(name="tool_disk", host="127.0.0.1", port=5001, timeout=30)
 
import os
BASE_DIR = os.environ.get("BASE_DIR", "c:/workspace/test")

# Folder creation tool
@mcp.tool()
def create_folder(folder_name: str) -> str:
    """
    Create a folder under BASE_DIR.
    """
    import os
 
    folder_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return f"Folder '{folder_name}' has been created."
    else:
        return f"Folder '{folder_name}' already exists."
  
# Folder deletion tool
@mcp.tool()
def delete_folder(folder_name: str) -> str:
    """
    Delete a folder under BASE_DIR.
    """
    import os
    import shutil

    folder_path = os.path.join(BASE_DIR, folder_name)
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        return f"Folder '{folder_name}' has been deleted."
    else:
        return f"Folder '{folder_name}' does not exist or is not a folder."
 
# File reading tool
@mcp.tool()
def read_file(file_name: str) -> str:
    """
    Read a file under BASE_DIR.
    """
    import os
 
    file_path = os.path.join(BASE_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        return f"Contents of file '{file_name}':\n{content}"
    else:
        return f"File '{file_name}' does not exist."
 
 
# File writing tool
@mcp.tool()
def write_file(file_name: str, content: str) -> str:
    """
    Write a file under BASE_DIR.
    """
    import os
 
    file_path = os.path.join(BASE_DIR, file_name)
    with open(file_path, "w") as f:
        f.write(content)
    return f"File '{file_name}' has been created."

# File deletion tool
@mcp.tool()
def delete_file(file_name: str) -> str:
    """
    Delete a file under BASE_DIR.
    """
    import os

    file_path = os.path.join(BASE_DIR, file_name)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        os.remove(file_path)
        return f"File '{file_name}' has been deleted."
    else:
        return f"File '{file_name}' does not exist or is not a file."

# Run the server
if __name__ == "__main__":
    mcp.run()