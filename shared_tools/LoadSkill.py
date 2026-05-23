from pathlib import Path

from agency_swarm.tools import BaseTool
from pydantic import Field


class LoadSkill(BaseTool):
    """
    Dynamically loads and reads the contents of a specialized skill from the skills/ repository.
    Use this when you need specialized knowledge (e.g., humanizing text, formatting)
    that is not included in your baseline prompt.
    """

    skill_name: str = Field(
        ...,
        description="The name of the skill to load (e.g., 'humanizer'). If set to 'list', returns a list of available skills.",
    )

    def run(self) -> str:
        project_root = Path(__file__).parent.parent
        skills_dir = project_root / "skills"

        if not skills_dir.exists():
            return "No skills directory found."

        if self.skill_name.lower() == "list":
            skills = [p.parent.name for p in skills_dir.glob("*/SKILL.md")]
            if not skills:
                return "No skills available."
            return "Available skills: " + ", ".join(skills)

        skill_file = skills_dir / self.skill_name / "SKILL.md"
        if not skill_file.exists():
            return f"Skill '{self.skill_name}' not found. Try 'list' to see available skills."

        with open(skill_file, encoding="utf-8") as f:
            content = f.read()

        return f"Loaded skill '{self.skill_name}':\n\n{content}"
