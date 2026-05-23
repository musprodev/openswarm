<div align="center">

# OpenSwarm

**Your AI-powered office. One prompt → complete deliverables.**

![OpenSwarm](assets/openswarm.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-≥3.12-blue)](https://python.org)
[![Node](https://img.shields.io/badge/Node-≥18-green)](https://nodejs.org)
[![Docker](https://img.shields.io/badge/Docker-ready-blue)](https://docker.com)
[![CLI](https://img.shields.io/badge/CLI-opencode-purple)](https://opencode.ai)

</div>

OpenSwarm is an **open-source multi-agent AI system** that acts as your entire office staff. Eight specialized agents collaborate through an intelligent orchestrator — research, write, analyze data, build slides, generate images, produce videos, and manage communications. All from a single prompt.

---

- [Features](#features)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Example Prompts](#example-prompts)
- [Architecture](#architecture)
- [Agent Reference](#agent-reference)
- [Configuration](#configuration)
- [OpenCode Integration](#opencode-integration)
- [Project Structure](#project-structure)
- [Development](#development)
- [Custom Swarms](#custom-swarms)
- [License](#license)

---

## Features

OpenSwarm replaces an entire office toolchain with a team of AI agents that hand off work to each other automatically.

### Agent Capabilities

| Agent | What it does |
|---|---|
| **Orchestrator** | Routes every request to the right specialist. Breaks complex tasks into parallel subtasks and assembles final output. |
| **Virtual Assistant** | Email, calendar, Slack, file management, task tracking. 10,000+ integrations via Composio (Gmail, Slack, GitHub, HubSpot, Google Calendar). |
| **Deep Research** | Comprehensive web research with citations. Competitive analysis, academic paper search, evidence-based synthesis. |
| **Data Analyst** | Spreadsheet analysis, charts, statistical models — all inside an isolated IPython kernel. pandas, numpy, scipy, scikit-learn, matplotlib, seaborn, plotly. |
| **Docs Agent** | Formatted Word documents and PDFs. Full document lifecycle: create, view, modify, convert, restore. |
| **Slides Agent** | Polished HTML slide decks with speaker notes, exported to PPTX. Themes, layouts, images, charts, custom styling. |
| **Image Agent** | Generate and edit images via Gemini and fal.ai. Combine, edit, background removal. |
| **Video Agent** | Produce videos via Sora, Veo, Seedance. Edit audio, add subtitles, combine clips, trim. |

### Platform Capabilities

- **Parallel execution** — agents work simultaneously on split tasks
- **File sharing** — agents pass documents, images, slides between each other
- **10,000+ integrations** — Gmail, Slack, GitHub, Google Calendar, HubSpot and more
- **Multi-provider** — OpenAI, Anthropic Claude, or Google Gemini
- **Graceful degradation** — missing API keys disable only the affected tools
- **Auto-bootstrap** — dependencies install themselves on first run

---

## Quick Start

### One-liner (recommended)

```bash
npm install -g @vrsen/openswarm && openswarm
```

The setup wizard handles everything: API keys, dependencies, configuration.

### From source

```bash
git clone https://github.com/musprodev/openswarm.git
cd openswarm
python swarm.py
```

### Docker

```bash
cp .env.example .env
docker-compose up --build
```

---

## Usage

### Terminal UI

```bash
openswarm
```

Launches the interactive terminal. Type a request and the orchestrator dispatches it to the right agents.

### API Server

```bash
python server.py
```

FastAPI server on `localhost:8080` with full API endpoints.

### Python module

```python
from swarm import create_agency

agency = create_agency()
agency.demo()
```

---

## Example Prompts

Paste these into the terminal:

```bash
"Create a quarterly report from last quarter's data — analyze the numbers, build charts, write the report, make a slide deck"

"Research our top 5 competitors and write 3 SEO-optimized blog posts with images"

"Build a Q2 marketing campaign — strategy doc, creative assets, social posts, and a promo video"

"Schedule a team standup for tomorrow, send the agenda via email, and prepare meeting notes"

"Create an investor pitch deck with market research, financial projections, and executive summary"
```

---

## Architecture

```
                    ┌─────────────┐
                    │    User     │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ Orchestrator│
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         │     Parallel    │    Execution     │
         ▼          ▼      ▼       ▼          ▼
   ┌──────────┐ ┌────────┐ ┌──────┐ ┌──────┐ ┌──────────┐
   │  Virtual │ │  Deep  │ │ Data │ │ Docs │ │  Slides  │
   │Assistant │ │Research│ │Analyst│ │Agent │ │  Agent   │
   └──────────┘ └────────┘ └──────┘ └──────┘ └──────────┘
   ┌──────────┐ ┌────────┐
   │  Image   │ │  Video │
   │  Agent   │ │  Agent │
   └──────────┘ └────────┘
```

Each agent is an independent module with its own tools, instructions, and model config. The orchestrator handles task splitting, distribution, and result assembly. Agents communicate through a shared tool system and can pass files to each other.

---

## Agent Reference

| Agent | Entry point | Tools |
|---|---|---|
| Orchestrator | `orchestrator/` | Handoff, SendMessage |
| Virtual Assistant | `virtual_assistant/` | Email, Calendar, Slack, Files, Search |
| Deep Research | `deep_research/` | Web search, Scholar search |
| Data Analyst | `data_analyst_agent/` | IPython kernel, pandas, matplotlib |
| Docs Agent | `docs_agent/` | Create/Modify/Convert/View documents |
| Slides Agent | `slides_agent/` | HTML slides, PPTX export |
| Image Agent | `image_generation_agent/` | Generate, Edit, Combine, Remove BG |
| Video Agent | `video_generation_agent/` | Generate, Edit, Combine, Subtitles |

---

## Configuration

### Required (choose one)

| Variable | Provider |
|---|---|
| `OPENAI_API_KEY` | OpenAI — GPT models + Sora video |
| `ANTHROPIC_API_KEY` | Anthropic — Claude models |
| `GOOGLE_API_KEY` | Google — Gemini models + Veo video |

### Optional

| Variable | What it unlocks |
|---|---|
| `COMPOSIO_API_KEY` | 10,000+ integrations (Gmail, Slack, GitHub, HubSpot) |
| `COMPOSIO_USER_ID` | User ID for Composio |
| `SEARCH_API_KEY` | Web search for Research Agent |
| `FAL_KEY` | Video editing, background removal |
| `PEXELS_API_KEY` | Stock photo search |
| `PIXABAY_API_KEY` | Stock photo search |
| `UNSPLASH_ACCESS_KEY` | Stock photo search |
| `DEFAULT_MODEL` | Override default model for all agents |

```bash
cp .env.example .env
```

Or use the interactive wizard:

```bash
python onboard.py
```

---

## OpenCode Integration

OpenSwarm can be used as an agent inside [OpenCode](https://opencode.ai):

```bash
opencode --agent openswarm
```

Or via `opencode.json`:

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

### Available sub-agents

| File | Role |
|---|---|
| `agents/openswarm.md` | Orchestrator — entry point |
| `agents/openswarm-coder.md` | Software engineering |
| `agents/openswarm-data-analyst.md` | Data analysis & visualization |
| `agents/openswarm-deep-research.md` | Web research & synthesis |
| `agents/openswarm-docs-agent.md` | Document creation |
| `agents/openswarm-formatter.md` | Formatting & export |
| `agents/openswarm-image-agent.md` | Image generation |
| `agents/openswarm-plagiarism.md` | Originality checking |
| `agents/openswarm-reviewer.md` | Review & QA |
| `agents/openswarm-slides-agent.md` | Slide decks |
| `agents/openswarm-video-agent.md` | Video production |
| `agents/openswarm-virtual-assistant.md` | Email, calendar, Slack |

---

## Project Structure

```
├── swarm.py                    # Agency config, agent imports, comm flows
├── server.py                   # FastAPI server
├── run_utils.py                # CLI bootstrap & auto-install
├── onboard.py                  # Setup wizard
├── config.py                   # Model configuration
├── helpers.py                  # Integration helpers
├── shared_instructions.md      # Cross-agent context
│
├── orchestrator/               # Orchestrator agent
├── virtual_assistant/          # Email, calendar, Slack, files
├── deep_research/              # Web research
├── data_analyst_agent/         # Data analysis & visualization
├── docs_agent/                 # Document creation
├── slides_agent/               # Slide decks & PPTX export
├── image_generation_agent/     # Image generation & editing
├── video_generation_agent/     # Video generation & editing
│
├── shared_tools/               # Cross-agent tool system
├── patches/                    # Runtime dependency patches
├── schemas/                    # JSON data models
├── tools/                      # State management, context
├── agents/                     # OpenCode agent definitions
├── docs/                       # Documentation
├── assets/                     # Branding assets
│
├── bin/openswarm               # npm entry point
├── docker-compose.yml          # Docker deployment
├── Dockerfile                  # Docker build
├── .env.example                # Environment template
├── .github/                    # CI/CD & issues
└── AGENTS.md                   # AI agent customization guide
```

---

## Development

### Requirements

- Python ≥ 3.12
- Node.js ≥ 18
- LibreOffice (for PPTX export)
- Poppler / pdftoppm (for slide thumbnails)

### Setup

```bash
git clone https://github.com/musprodev/openswarm.git
cd openswarm
cp .env.example .env
pip install -e .
npm install
```

---

## Custom Swarms

Fork this repo and reshape it for any domain. Tell your coding agent:

> "Turn this into an SEO optimization swarm."

The agent reads `AGENTS.md` and rewires everything automatically.

**Ready-made ideas:**
- **SEO Swarm** — keyword research, competitor analysis, blog writing
- **Sales Swarm** — lead research, outreach sequencing, proposal generation
- **Marketing Swarm** — campaign planning, creative assets, analytics
- **Academic Swarm** — research writing, formatting, bibliography

---

## License

MIT — see [LICENSE](LICENSE).
