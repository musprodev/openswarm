import os
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

os.makedirs(".pi/agents", exist_ok=True)

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
            
    # Pi Agent format
    md_content = f"""# Role: {agent['name'].replace('_', ' ').title()} OpenSwarm Agent

{instructions}
{shared}
"""
    # Adjust references for Pi Agent CLI
    md_content = md_content.replace("via OpenCode", "via Pi")
    md_content = md_content.replace("OpenCode tools", "Pi tools")
    md_content = md_content.replace("OpenCode environment", "Pi environment")

    # Replace agency-swarm specific text like Handoff / SendMessage to use Pi instructions
    if agent["name"] == "orchestrator":
        md_content = md_content.replace("use `Handoff`", "delegate using Pi tools")
        md_content = md_content.replace("use `SendMessage`", "delegate using Pi tools")
        md_content = md_content.replace("Handoff", "delegation")
        md_content = md_content.replace("SendMessage", "delegation")
        md_content = md_content.replace("transfer tool", "delegation")
        
    out_path = Path(".pi/agents") / f"openswarm-{agent['name'].replace('_', '-')}.md"
    
    if agent["name"] == "orchestrator":
        out_path = Path(".pi/agents") / "openswarm.md"
        
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"Created {out_path}")
