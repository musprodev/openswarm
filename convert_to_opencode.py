import os
import glob
from pathlib import Path

# Agents to convert
agents_to_convert = [
    {"name": "orchestrator", "folder": "orchestrator", "mode": "all"},
    {"name": "virtual_assistant", "folder": "virtual_assistant", "mode": "subagent"},
    {"name": "deep_research", "folder": "deep_research", "mode": "subagent"},
    {"name": "data_analyst", "folder": "data_analyst_agent", "mode": "subagent"},
    {"name": "docs_agent", "folder": "docs_agent", "mode": "subagent"},
    {"name": "slides_agent", "folder": "slides_agent", "mode": "subagent"},
    {"name": "image_agent", "folder": "image_generation_agent", "mode": "subagent"},
    {"name": "video_agent", "folder": "video_generation_agent", "mode": "subagent"}
]

os.makedirs("agents", exist_ok=True)

for agent in agents_to_convert:
    inst_path = Path(agent["folder"]) / "instructions.md"
    if not inst_path.exists():
        print(f"Skipping {agent['name']}, no instructions.md")
        continue
        
    with open(inst_path, "r", encoding="utf-8") as f:
        instructions = f.read()
        
    # Read shared_instructions.md if it's not the orchestrator
    shared = ""
    if agent["name"] != "orchestrator":
        try:
            with open("shared_instructions.md", "r", encoding="utf-8") as f:
                shared = f"\n\n# Shared Context\n\n" + f.read()
        except Exception:
            pass
            
    # For opencode agent format
    md_content = f"""---
description: {agent['name'].replace('_', ' ').title()} OpenSwarm Agent
mode: {agent['mode']}
---
{instructions}
{shared}
"""
    # Replace agency-swarm specific text like Handoff / SendMessage to use opencode Task tool
    if agent["name"] == "orchestrator":
        md_content = md_content.replace("use `Handoff`", "delegate using the Task tool")
        md_content = md_content.replace("use `SendMessage`", "delegate using the Task tool")
        md_content = md_content.replace("Handoff", "Task tool")
        md_content = md_content.replace("SendMessage", "Task tool")
        md_content = md_content.replace("transfer tool", "Task tool")
        
    out_path = Path("agents") / f"openswarm-{agent['name'].replace('_', '-')}.md"
    
    if agent["name"] == "orchestrator":
        out_path = Path("agents") / "openswarm.md"
        
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"Created {out_path}")
