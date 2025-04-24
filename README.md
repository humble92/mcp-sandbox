# MCP Sandbox Project

## Description

This project is a sandbox environment showcasing various tools and functionalities implemented using the Model Context Protocol (MCP) and the `FastMCP` library. It includes several independent MCP servers, each providing specific capabilities.

## Features / Components

This project includes the following MCP servers:

*   **`tool_greeting.py`**: Provides simple tools like `echo` and a `greeting` tool that uses a dynamic resource.
*   **`tool_disk.py`**: Offers tools for basic disk operations like creating/deleting folders and reading/writing/deleting files within a base directory (`c:/workspace/test`).
*   **`tool_excel.py`**: Includes a tool to create Excel files (`.xlsx`) with specified content in the base directory (`c:/workspace/test`).
*   **`tool_keyboard.py`**: Provides a tool to control the keyboard, specifically to type a message into Notepad.
*   **`tool_hwp.py`**: Contains a tool to read text content from Hangul Word Processor (`.hwp`) files located in the base directory (`c:/workspace/test`).
*   **`tool_math.py`**: A simple server with an `add` tool and a dynamic `goodbye` resource.
*   **`prompts.py`**: Defines custom prompts (`prompt_decision`, `prompt_opinion`) that can be used with language models.
*   **`resource_agent.py`**: Implements a resource (`Agent://state`) to retrieve the state of an AI agent.
*   **`main.py`**: A simple placeholder script.

## Setup

1.  **Prerequisites**: Ensure you have Python (>=3.12) and `uv` installed.
2.  **Dependencies**: Install the required Python packages listed in `pyproject.toml`. You can typically do this using `uv`:
    ```bash
    uv pip install -r requirements.txt 
    ```
    (You might need to generate `requirements.txt` from `pyproject.toml` first using `uv pip freeze > requirements.txt` or install directly using `uv pip install .` if your setup supports it).

## Usage

Each MCP server can be run individually. The configuration in `~\.cursor\mcp.json` suggests these servers are intended to be launched via `uv`. See `save/claude_desktop_config.json` for reference.

To run a specific server manually (example):

```bash
uv run tool_greeting.py
mcp dev tool_greeting.py
```

Replace `tool_greeting.py` with the script name of the server you want to run. These servers can then be accessed by MCP clients or frameworks that integrate with MCP.

## Configuration

*   **Base Directories**: Some tools (`tool_disk.py`, `tool_excel.py`, `tool_hwp.py`) operate within a specific base directory (`c:/workspace/test`). Ensure this directory exists or modify the `BASE_DIR` constant in the respective scripts if needed.
*   **Server Ports**: Each server is configured to run on a specific port (e.g., `tool_greeting` on 5000, `tool_disk` on 5001, etc.). Ensure these ports are available.

# References

## MCP SDK
* https://github.com/modelcontextprotocol
* https://github.com/modelcontextprotocol/swift-sdk

## MCP server repos
* https://github.com/modelcontextprotocol/servers/tree/main
* https://mcp.so
* https://smithery.ai

## MCP framework or extentions.
* https://fast-agent.ai (fast-agent - MCP native Agents and Workflows)
* https://github.com/langchain-ai/langchain-mcp-adapters (Langchain)
* https://github.com/tadata-org/fastapi_mcp (FastAPI)
* https://www.youtube.com/watch?v=eczLRG3q4V0 (Flutter)
* (cf) https://github.com/settings/copilot

## Use cases of 3rd parties
* https://gitmcp.io (Instantly create a Remote MCP server for any GitHub repository)
* https://github.com/elevenlabs/elevenlabs-mcp/tree/main (elevenlabs)
* https://docs.windsurf.com/windsurf/mcp
* https://www.youtube.com/watch?v=dutyOc_cAEU (VS code)
* https://gist.github.com/burkeholland/24802296b5bfaaf7fb775c81cd626512

## Other references
* https://modelcontextprotocol.io/quickstart/server
* https://www.books.weniv.co.kr/basecamp-mcp
* https://modelcontextprotocol.io/clients (Feature support matrix)
* https://www.youtube.com/watch?v=EswVjHZMn74

## Roadmap:
* https://modelcontextprotocol.io/development/roadmap
* OAuth Authentication (not API keys)
* MCP registry