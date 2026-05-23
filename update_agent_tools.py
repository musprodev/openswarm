import os
import glob
from pathlib import Path

agents_to_convert = [
    {"name": "virtual_assistant", "folder": "virtual_assistant"},
    {"name": "deep_research", "folder": "deep_research"},
    {"name": "data_analyst", "folder": "data_analyst_agent"},
    {"name": "docs_agent", "folder": "docs_agent"},
    {"name": "slides_agent", "folder": "slides_agent"},
    {"name": "image_agent", "folder": "image_generation_agent"},
    {"name": "video_agent", "folder": "video_generation_agent"}
]

for agent in agents_to_convert:
    out_path = Path("agents") / f"openswarm-{agent['name'].replace('_', '-')}.md"
    if not out_path.exists():
        continue
        
    # Get list of tools
    tools_dir = Path(agent["folder"]) / "tools"
    tools_list = []
    if tools_dir.exists():
        for py_file in tools_dir.glob("*.py"):
            if py_file.name != "__init__.py" and py_file.name != "deck_utils.py" and py_file.name != "slide_file_utils.py":
                tools_list.append(py_file.stem)
                
    tool_instruction = "\n\n### Access to OpenSwarm Tools\n"
    tool_instruction += "You have access to the legacy OpenSwarm python tools. To use them, write and execute a short python script using the `bash` tool.\n"
    tool_instruction += "Example:\n```python\n"
    tool_instruction += f"from {agent['folder']}.tools.ToolName import ToolName\n"
    tool_instruction += "tool = ToolName(arg1='value')\n"
    tool_instruction += "print(tool.run())\n```\n"
    if tools_list:
        tool_instruction += "Available tools for this agent:\n"
        for t in tools_list:
            tool_instruction += f"- {t}\n"
            
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(tool_instruction)
        
    print(f"Updated {out_path} with tools.")
