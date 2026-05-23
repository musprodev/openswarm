import os
from pathlib import Path

agents_to_convert = [
    "openswarm-virtual-assistant.md",
    "openswarm-deep-research.md",
    "openswarm-data-analyst.md",
    "openswarm-docs-agent.md",
    "openswarm-slides-agent.md",
    "openswarm-image-agent.md",
    "openswarm-video-agent.md"
]

shared_tools_list = []
shared_tools_dir = Path("shared_tools")
if shared_tools_dir.exists():
    for py_file in shared_tools_dir.glob("*.py"):
        if py_file.name != "__init__.py" and py_file.name != "model_availability.py" and py_file.name != "openai_client_utils.py":
            shared_tools_list.append(py_file.stem)

if shared_tools_list:
    shared_instruction = "\n\n### Access to Shared OpenSwarm Tools\n"
    shared_instruction += "You also have access to shared tools in the `shared_tools` package. You can run them via python script just like your specific tools:\n"
    shared_instruction += "```python\n"
    shared_instruction += f"from shared_tools.ToolName import ToolName\n"
    shared_instruction += "tool = ToolName(arg1='value')\n"
    shared_instruction += "print(tool.run())\n```\n"
    shared_instruction += "Available shared tools:\n"
    for t in shared_tools_list:
        shared_instruction += f"- {t}\n"
        
    for agent_file in agents_to_convert:
        out_path = Path("agents") / agent_file
        if out_path.exists():
            with open(out_path, "a", encoding="utf-8") as f:
                f.write(shared_instruction)
            print(f"Updated {out_path} with shared tools.")
