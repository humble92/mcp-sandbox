from mcp.server.fastmcp import FastMCP
 
# MCP server
mcp = FastMCP(name="tool_excel", host="127.0.0.1", port=5003, timeout=30)
 
BASE_DIR = "c:/workspace/test"

# Organize the table input by Excel writer
@mcp.tool()
def write_excel(contents: list, file_name: str) -> str:
    """
    Create an Excel file under BASE_DIR.
    """
    # pip install xlsxwriter
    # Create an Excel file (file_name)
 
    import os
    import xlsxwriter
 
    file_path = os.path.join(BASE_DIR, file_name)
 
    workbook = xlsxwriter.Workbook(file_path)
 
    # Create a worksheet inside the file (created with the name 'test', multiple worksheets can be created)
    worksheet = workbook.add_worksheet("test")
 
    # Write data to Excel
    for row_num, row_data in enumerate(contents):
        for col_num, value in enumerate(row_data.values()):
            worksheet.write(row_num, col_num, value)
 
    # Save the Excel file
    workbook.close()
    return f"Excel file '{file_path}' has been created."
 
 
# Run the server
if __name__ == "__main__":
    mcp.run()