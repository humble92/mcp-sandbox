from mcp.server.fastmcp import FastMCP
 
# MCP server
mcp = FastMCP(name="tool_hwp", host="127.0.0.1", port=5011, timeout=30)
  
import os
BASE_DIR = os.environ.get("BASE_DIR", "c:/workspace/test")

# Read Hangul document
@mcp.tool()
def read_hwp(file_name: str) -> str:
    """
    Read a Hangul document (.hwp) and return the text.

    Uses the olefile library to extract text content from a Hangul document.

    Args:
        file_name (str): Name of the Hangul document to read
            Example: 'document.hwp'

    Returns:
        str: Extracted text content from the Hangul document or an error message
    """
    import os
    import olefile
 
    # You need to install olefile
 
    # Convert to absolute path based on the current directory if it's a relative path
    file_path = os.path.join(BASE_DIR, file_name)
 
    try:
        # Open Hangul file
        if not olefile.isOleFile(file_path):
            return f"Error: '{file_path}' is not a valid Hangul document format."
 
        ole = olefile.OleFileIO(file_path)
 
        # Attempt to read text stream
        if ole.exists("PrvText"):
            text_stream = ole.openstream("PrvText")
            text_data = text_stream.read().decode("utf-16-le", errors="replace")
            ole.close()
            return text_data
 
        # Alternative attempt if preview text is not available
        elif ole.exists("BodyText/Section0"):
            section = ole.openstream("BodyText/Section0")
            data = section.read()
            ole.close()
 
            # Simple text extraction (may not be complete)
            result = ""
            for i in range(0, len(data), 2):
                if i + 1 < len(data):
                    code = data[i] + (data[i + 1] << 8)
                    if code > 31 and code < 127:
                        result += chr(code)
                    elif code > 255:
                        result += chr(code)
                    else:
                        result += " "
 
            return result
 
        else:
            ole.close()
            return "Cannot extract text content. It may be an unsupported Hangul document format."
 
    except Exception as e:
        return f"Error reading Hangul document: {str(e)}"
 
 
# Run the server
if __name__ == "__main__":
    mcp.run()