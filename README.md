<div align="center">

# 🏢 OpenSwarm — OFFICE AI Agent

![OpenSwarm](assets/new-framework.jpg)

</div>

**Your AI-powered office team. From one prompt to complete deliverables.**

OpenSwarm is a multi-agent AI system that acts as your entire office staff — research, write, analyze data, build slides, generate images, produce videos, and manage communications. All from a single prompt in your terminal.

✨ **One prompt → Complete office deliverables**<br>
🎯 **8 specialized AI agents working together**<br>
⚡ **Install in 30 seconds, running in 60**<br>
🔧 **100% customizable — fork and build your own swarm**<br>

Built on [Agency Swarm](https://github.com/VRSEN/agency-swarm) — the open-source multi-agent framework.

---

## 💡 What Is an OFFICE AI Agent?

Instead of switching between ChatGPT, Canva, Excel, and Google Docs, you get **specialists coordinated by an orchestrator** — working together to produce complete deliverables.

### 🎯 Real Office Tasks

Paste these into your terminal:

- **"Draft a quarterly report with charts from last quarter's data"** → Analysis + visualizations + formatted document
- **"Research our top 5 competitors and write blog posts"** → Competitive analysis + keyword research + publish-ready content
- **"Create an investor pitch deck and executive summary"** → Full slides + written summary + market research
- **"Schedule a team meeting and send the agenda via email"** → Calendar management + Slack/email notifications
- **"Generate product launch images and a promo video"** → Professional graphics + animated video with transitions

---

## 🤖 Meet Your Office AI Team

| Agent | What it does |
|---|---|
| **Orchestrator** | Routes every request to the right specialist. Pure coordination. |
| **Virtual Assistant** | Email, calendar, Slack, file management, task tracking. 10,000+ integrations via Composio (Gmail, Slack, GitHub, HubSpot). |
| **Deep Research** | Comprehensive web research with citations, competitive analysis, and balanced synthesis. |
| **Data Analyst** | Analyzes spreadsheets, builds charts, runs statistical models — all in an isolated IPython kernel. |
| **Docs Agent** | Creates formatted Word documents, PDFs, reports, and meeting notes. |
| **Slides Agent** | Generates polished HTML slide decks and exports to PPTX. |
| **Image Generation Agent** | Creates and edits images using Gemini and fal.ai models. |
| **Video Generation Agent** | Produces and edits videos via Sora, Veo, and Seedance. |

---

## 📦 Get Started

```bash
npm install -g @vrsen/openswarm
openswarm
```

The setup wizard handles authentication, dependencies, and configuration.

**Requirements:** Node.js 20+ (Python 3.10+ auto-installed)

## 🔧 Local Development

```bash
git clone https://github.com/musprodev/openswarm.git
cd openswarm
python swarm.py
```

**Docker:**
```bash
cp .env.example .env        # Add your API keys
docker-compose up --build
```

**API server:**
```bash
python server.py           # Runs on localhost:8080
```

## ⚙️ Requirements

**At least one of:**
- `OPENAI_API_KEY` — GPT models + Sora video
- `ANTHROPIC_API_KEY` — Claude models

**Optional:**
- `COMPOSIO_API_KEY` — 10,000+ integrations (Gmail, Slack, GitHub)
- `GOOGLE_API_KEY` — Gemini image generation + Veo video
- `FAL_KEY` — Advanced video editing
- `SEARCH_API_KEY` — Web search for research agent

---

## 🏗️ Build Your Own Swarm

Fork this repo and create a custom AI team:

> _"Turn this into an SEO optimization swarm"_ — Claude Code, Cursor, or Codex will customize all agents automatically.

**Popular custom swarms:**
- **SEO Swarm** — Keyword research + competitor analysis + blog writing
- **Sales Swarm** — Lead research + outreach + proposal generation
- **Marketing Swarm** — Campaign planning + creative assets + analytics
- **Product Swarm** — Market research + feature specs + launch materials

---

## 📄 License

MIT — see [LICENSE](LICENSE).

**Built with ❤️ by the team behind [Agency Swarm](https://github.com/VRSEN/agency-swarm)**
