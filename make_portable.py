import os
import re
from pathlib import Path

PROJECT_ROOT = "/home/hashira/Tools/openswarm"
GLOBAL_AGENT_DIR = Path.home() / ".config" / "opencode" / "agents"

def make_portable():
    if not GLOBAL_AGENT_DIR.exists():
        print(f"Global agent dir {GLOBAL_AGENT_DIR} not found.")
        return

    for agent_file in GLOBAL_AGENT_DIR.glob("openswarm*.md"):
        with open(agent_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Update python script calls to absolute paths
        content = content.replace("python tools/state_manager.py", f"python {PROJECT_ROOT}/tools/state_manager.py")
        content = content.replace("python tools/context_retriever.py", f"python {PROJECT_ROOT}/tools/context_retriever.py")
        
        # Update example python snippets (imports)
        # We need to add the project root to sys.path in the example snippets
        import_fix = f"import sys; sys.path.append('{PROJECT_ROOT}'); "
        
        # Look for the python code blocks and inject sys.path
        def inject_sys_path(match):
            block = match.group(1)
            if "from " in block or "import " in block:
                if PROJECT_ROOT not in block:
                    return f"```python\n{import_fix}{block}```"
            return f"```python\n{block}```"

        content = re.sub(r"```python\n(.*?)```", inject_sys_path, content, flags=re.DOTALL)

        with open(agent_file, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Made {agent_file.name} portable.")

if __name__ == "__main__":
    make_portable()
