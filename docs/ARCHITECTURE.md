# OpenSwarm Academic Architecture

This document describes the OpenCode implementation of the OpenSwarm multi-agent system, specifically tailored for end-to-end university assignments.

## System Overview

The system is designed to break down complex, multi-domain university assignments into manageable tasks, route them to specialized agents, track state persistently, and ultimately deliver a packaged, formatted assignment ready for submission.

## Core Components

### 1. The Orchestrator (`agents/openswarm.md`)
- **Role**: The entry point.
- **Responsibilities**:
  - Ingests the user prompt.
  - Queries `tools/context_retriever.py` for course syllabi or global preferences.
  - Generates a task plan and saves it using `tools/state_manager.py`.
  - Delegates tasks to specific sub-agents using the Task tool.
  - Handles the recovery loop (feeding errors/critiques back to sub-agents).

### 2. State & Memory Management
- **State Store (`workflows/`)**: Managed by `tools/state_manager.py`. Keeps track of `assignment_id`, `objective`, and individual task statuses (`pending`, `in_progress`, `completed`, `failed`). Allows the swarm to resume work if interrupted.
- **Memory (`memory/`)**: Managed by `tools/context_retriever.py`. Stores long-term user preferences (e.g., "Always use APA formatting") and course-specific contexts.

### 3. Specialized Sub-Agents

1. **Deep Research Agent (`openswarm-deep-research`)**:
   - Searches the web and scholar databases.
   - Outputs structured, cited artifacts (e.g., `research_notes.md`, `bibliography.md`).
2. **Data Analyst (`openswarm-data-analyst`)**:
   - Uses Python to process data, generate charts, and solve academic math/statistics problems.
   - Outputs charts, `computation_results.md`, and CSV files.
3. **Coder (`openswarm-coder`)**:
   - Analyzes repositories, writes code, and executes test-driven debugging loops.
4. **Docs Agent (`openswarm-docs-agent`)**:
   - Ingests research/data artifacts to draft essays and reports following an Outline -> Draft -> Critique -> Revise workflow.
5. **Slides Agent (`openswarm-slides-agent`)**:
   - Ingests artifacts to generate structured HTML/PPTX slide decks complete with comprehensive speaker notes.
6. **Virtual Assistant (`openswarm-virtual-assistant`)**:
   - Handles email, scheduling, and external tool integrations via Composio.
7. **Reviewer / QA (`openswarm-reviewer`)**:
   - Acts as a strict professor. Ingests grading rubrics and final deliverables to generate a Pass/Fail critique.
8. **Formatter / Exporter (`openswarm-formatter`)**:
   - Converts approved drafts into strict academic formats (LaTeX, Markdown to PDF).
   - Enforces university naming conventions and zips the final deliverables.

## Workflow Example

1. **User Request**: "Write a 5-page research paper on CRISPR for Bio101, create a slide deck, and package it."
2. **Orchestrator**: Creates `bio101_crispr` state. Assigns Task 1 to Research Agent.
3. **Research Agent**: Creates `research_notes.md`.
4. **Orchestrator**: Updates state, assigns Task 2 to Docs Agent and Task 3 to Slides Agent.
5. **Docs/Slides Agents**: Generate drafts and slides based on `research_notes.md`.
6. **Orchestrator**: Assigns Task 4 to Reviewer Agent.
7. **Reviewer**: Grades the drafts against the prompt. Passes.
8. **Orchestrator**: Assigns Task 5 to Formatter Agent.
9. **Formatter**: Zips the PDF, PPTX, and Bib files into `Lastname_Bio101_CRISPR.zip`.
10. **Orchestrator**: Completes the assignment and notifies the user.
