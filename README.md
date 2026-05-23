<div align="center">

# OpenSwarm — OFFICE AI Agent

![OpenSwarm](assets/new-framework.jpg)

**Your AI-powered office team. From a single prompt to complete deliverables.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-≥3.12-blue)](https://python.org)
[![Node](https://img.shields.io/badge/node-≥18-green)](https://nodejs.org)

OpenSwarm is an **open-source multi-agent AI system** that acts as your entire office staff — research, write, analyze data, build slides, generate images, produce videos, and manage communications. Eight specialized agents collaborate through an orchestrator to produce complete deliverables from one prompt.

Built on [Agency Swarm](https://github.com/VRSEN/agency-swarm) and the OpenAI Agents SDK.

---

## Features

| # | Agent | Capabilities |
|---|-------|-------------|
| 1 | **Orchestrator** | Routes every request to the right specialist. Pure coordination — never answers directly. Breaks complex tasks into parallel subtasks. |
| 2 | **Virtual Assistant** | Email, calendar, Slack, file management, task tracking. Connects to 10,000+ external services via Composio (Gmail, Slack, GitHub, HubSpot, Google Calendar, and more). |
| 3 | **Deep Research** | Comprehensive web research with citations. Competitive analysis, academic paper searches, and balanced evidence-based synthesis. |
| 4 | **Data Analyst** | Analyzes spreadsheets, builds charts, runs statistical models — all inside an isolated IPython kernel. Supports pandas, numpy, scipy, scikit-learn, matplotlib, seaborn, plotly. |
| 5 | **Docs Agent** | Creates formatted Word documents and PDFs from outlines or raw content. Full document lifecycle: create, view, modify, convert, restore. |
| 6 | **Slides Agent** | Generates polished HTML slide decks with speaker notes, then exports to PPTX. Supports themes, layouts, images, charts, and custom styling. |
| 7 | **Image Generation Agent** | Generates and edits images using Gemini 2.5 Flash Image / Gemini 3 Pro Image and fal.ai. Supports combine, edit, and background removal. |
| 8 | **Video Generation Agent** | Produces videos via Sora (OpenAI), Veo (Google), and Seedance (fal.ai). Edit audio, add subtitles, combine clips, trim, and generate images for video. |

### Key Capabilities

- **Parallel execution** — orchestrator splits complex tasks across multiple agents simultaneously
- **File attachments** — agents share documents, images, slides, and data files
- **10,000+ integrations** — Gmail, Slack, GitHub, Google Calendar, HubSpot, and more via Composio
- **Dual model support** — works with OpenAI, Anthropic Claude, or Google Gemini
- **Graceful degradation** — tools disable themselves when API keys are missing
- **Auto-bootstrap** — dependencies install automatically on first run

---

## Installation

### Quick Install (recommended)

```bash
npm install -g @vrsen/openswarm
openswarm
```

The setup wizard handles authentication, dependencies, and configuration automatically.

### From Source

```bash
git clone https://github.com/musprodev/openswarm.git
cd openswarm
python swarm.py
```

### Docker

```bash
cp .env.example .env        # Add your API keys
docker-compose up --build
```

### Python (pip)

```bash
pip install open-swarm
openswarm
```

---

## Usage

### Terminal UI (default)

```bash
openswarm
```

Launches the interactive terminal UI. Type your request and the orchestrator routes it to the right agents.

### API Server

```bash
python server.py
```

Starts a FastAPI server on `localhost:8080` with full Agency Swarm API endpoints.

### OpenCode Agent

Use OpenSwarm as an agent inside [OpenCode](https://opencode.ai):

```bash
opencode --agent openswarm
```

Or reference it from your `opencode.json`:

```json
{
  "agents": {
    "openswarm": {
      "description": "Multi-agent OFFICE AI team",
      "path": "/path/to/openswarm/agents/openswarm.md"
    }
  }
}
```

Available sub-agents:

| Agent file | Purpose |
|---|---|
| `agents/openswarm.md` | Orchestrator — entry point, routes tasks |
| `agents/openswarm-coder.md` | Coding and software engineering |
| `agents/openswarm-data-analyst.md` | Data analysis and visualization |
| `agents/openswarm-deep-research.md` | Web research and synthesis |
| `agents/openswarm-docs-agent.md` | Document creation and editing |
| `agents/openswarm-formatter.md` | Formatting and export |
| `agents/openswarm-image-agent.md` | Image generation and editing |
| `agents/openswarm-plagiarism.md` | Plagiarism and originality checking |
| `agents/openswarm-reviewer.md` | Review and QA |
| `agents/openswarm-slides-agent.md` | Slide deck generation |
| `agents/openswarm-video-agent.md` | Video generation and editing |
| `agents/openswarm-virtual-assistant.md` | Email, calendar, Slack, files |

### Example Prompts

```bash
# Full office workflow
"Create a quarterly report for last quarter's sales data — analyze the numbers, build charts, write the report, and make a slide deck"

# Research + content
"Research our top 5 competitors and write 3 SEO-optimized blog posts with images"

# Marketing campaign
"Build a Q2 marketing campaign — strategy doc, creative assets, social posts, and a promo video"

# Meeting + follow-up
"Schedule a team standup for tomorrow, send the agenda via email, and prepare meeting notes template"

# Investor materials
"Create an investor pitch deck with market research, financial projections, and an executive summary document"
```

---

## Architecture

```
┌─────────────┐
│    User     │
└──────┬──────┘
       │
┌──────▼──────┐
│ Orchestrator│  Routes work to specialists
└──────┬──────┘
       │
       ├──────────────────────────────────┐
       │        Parallel Execution        │
       ├────────┬────────┬───────┬───────┤
       ▼        ▼        ▼       ▼       ▼
┌─────────┐ ┌──────┐ ┌────┐ ┌────┐ ┌──────┐
│ Virtual │ │Deep  │ │Data│ │Docs│ │Slides│
│ Assis-  │ │Rese- │ │Ana-│ │Age-│ │Agent │
│ tant    │ │arch  │ │lyst│ │nt  │ │      │
└─────────┘ └──────┘ └────┘ └────┘ └──────┘
┌─────────┐ ┌──────┐ ┌────┐
│ Image   │ │Video │ │... │
│ Agent   │ │Agent │ │More│
└─────────┘ └──────┘ └────┘
```

Each agent operates independently with its own tools, instructions, and model configuration. The orchestrator splits complex tasks, distributes them, and assembles the final output.

---

## Configuration

### Required (choose at least one)

| Variable | Provider |
|---|---|
| `OPENAI_API_KEY` | OpenAI — GPT models + Sora video |
| `ANTHROPIC_API_KEY` | Anthropic — Claude models |
| `GOOGLE_API_KEY` | Google — Gemini models + Veo video |

### Optional

| Variable | What it unlocks |
|---|---|
| `COMPOSIO_API_KEY` | 10,000+ integrations (Gmail, Slack, GitHub, HubSpot) |
| `SEARCH_API_KEY` | Web search for Research Agent |
| `FAL_KEY` | Advanced video editing, background removal |
| `PEXELS_API_KEY` | Stock photo search |
| `PIXABAY_API_KEY` | Stock photo search |
| `UNSPLASH_ACCESS_KEY` | Stock photo search |
| `DEFAULT_MODEL` | Override the default model for all agents |

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

Or run the setup wizard:

```bash
python onboard.py
```

---

## Development

### Requirements

- Python ≥ 3.12
- Node.js ≥ 18
- LibreOffice (for slides export)
- Poppler (for PDF thumbnails)

### Setup

```bash
git clone https://github.com/musprodev/openswarm.git
cd openswarm
cp .env.example .env     # Add your API keys
pip install -e .         # Install Python deps
npm install              # Install Node deps
```

### Project Structure

```
├── swarm.py                     # Main config — agent imports, communication flows
├── server.py                    # FastAPI entry point
├── run_utils.py                 # CLI bootstrap and auto-install
├── onboard.py                   # Interactive setup wizard
├── config.py                    # Model configuration
├── helpers.py                   # Composio integration helpers
├── shared_instructions.md       # Context shared across all agents
│
├── orchestrator/                # Orchestrator agent
├── virtual_assistant/           # Email, calendar, Slack, files
├── deep_research/               # Web research and synthesis
├── data_analyst_agent/          # Data analysis and visualization
├── docs_agent/                  # Document creation
├── slides_agent/                # Slide deck generation
├── image_generation_agent/      # Image generation and editing
├── video_generation_agent/      # Video generation and editing
│
├── shared_tools/                # Cross-agent tools
├── patches/                     # Runtime patches for dependencies
├── schemas/                     # JSON data models
├── tools/                       # Utility tools (state, context)
├── agents/                      # OpenCode agent definitions
├── docs/                        # Documentation
│
├── .github/                     # CI/CD workflows and issue templates
├── bin/openswarm                # npm launcher
├── docker-compose.yml           # Docker deployment
└── Dockerfile                   # Docker build
```

---

## Build Your Own Swarm

Fork this repo and customize it for any domain. Tell your AI coding agent:

> "Turn this into an SEO optimization swarm"

The agent reads `AGENTS.md`, understands the structure, and rewires everything automatically.

**Popular custom swarms:**
- **SEO Swarm** — Keyword research + competitor analysis + blog writing
- **Sales Swarm** — Lead research + outreach + proposal generation
- **Marketing Swarm** — Campaign planning + creative assets + analytics
- **Academic Swarm** — Research paper writing + formatting + bibliography

---

## License

MIT — see [LICENSE](LICENSE).

Built with ❤️ on [Agency Swarm](https://github.com/VRSEN/agency-swarm).
