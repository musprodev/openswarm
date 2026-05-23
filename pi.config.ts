import * as fs from "fs";
import * as path from "path";

function getPrompt(filename: string): string {
    const filePath = path.join(__dirname, ".pi", "agents", filename);
    try {
        return fs.readFileSync(filePath, "utf-8");
    } catch (e) {
        console.warn(`Warning: Could not read ${filePath}`);
        return `Error loading prompt: ${e}`;
    }
}

export default {
    agents: {
        "openswarm": {
            name: "OpenSwarm Orchestrator",
            description: "Main orchestrator for OpenSwarm. Routes tasks and manages assignments.",
            systemPrompt: getPrompt("openswarm.md")
        },
        "openswarm-data-analyst": {
            name: "OpenSwarm Data Analyst",
            description: "Data analysis, visualization, and statistical modeling.",
            systemPrompt: getPrompt("openswarm-data-analyst.md")
        },
        "openswarm-deep-research": {
            name: "OpenSwarm Deep Research",
            description: "Web research and synthesis.",
            systemPrompt: getPrompt("openswarm-deep-research.md")
        },
        "openswarm-docs-agent": {
            name: "OpenSwarm Docs Agent",
            description: "Document creation and editing.",
            systemPrompt: getPrompt("openswarm-docs-agent.md")
        },
        "openswarm-image-agent": {
            name: "OpenSwarm Image Agent",
            description: "AI image generation and editing.",
            systemPrompt: getPrompt("openswarm-image-agent.md")
        },
        "openswarm-slides-agent": {
            name: "OpenSwarm Slides Agent",
            description: "PowerPoint and HTML slide generation.",
            systemPrompt: getPrompt("openswarm-slides-agent.md")
        },
        "openswarm-video-agent": {
            name: "OpenSwarm Video Agent",
            description: "AI video generation and editing.",
            systemPrompt: getPrompt("openswarm-video-agent.md")
        },
        "openswarm-virtual-assistant": {
            name: "OpenSwarm Virtual Assistant",
            description: "Email, calendar, Slack, and file management.",
            systemPrompt: getPrompt("openswarm-virtual-assistant.md")
        }
    }
};
