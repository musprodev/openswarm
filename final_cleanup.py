import os
from pathlib import Path

def update_agents():
    # Read new shared instructions
    with open("shared_instructions.md", "r", encoding="utf-8") as f:
        new_shared = f.read()
    
    agent_dir = Path("agents")
    for agent_file in agent_dir.glob("*.md"):
        # Skip the orchestrator which might have a different structure
        if agent_file.name == "openswarm.md":
            continue
            
        with open(agent_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "# Shared Context" not in content:
            print(f"Skipping {agent_file.name}, no Shared Context header.")
            continue
            
        # Keep everything before "# Shared Context"
        base_content = content.split("# Shared Context")[0]
        
        # We also want to preserve the "Access to OpenSwarm Tools" sections 
        # which were at the very bottom.
        tool_sections = ""
        if "### Access to OpenSwarm Tools" in content:
            tool_sections += "\n\n### Access to OpenSwarm Tools" + content.split("### Access to OpenSwarm Tools")[1]
        elif "### Access to Shared OpenSwarm Tools" in content:
            # Handle cases where only shared tools exist or were appended differently
            tool_sections += "\n\n### Access to Shared OpenSwarm Tools" + content.split("### Access to Shared OpenSwarm Tools")[1]

        new_content = base_content + "# Shared Context\n\n" + new_shared + tool_sections
        
        with open(agent_file, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Updated {agent_file.name}")

if __name__ == "__main__":
    update_agents()
