# Implementation Plan: RepoGuide Core Breakdown

**Branch**: `001-repoguide-breakdown` | **Date**: 2026-03-30 | **Spec**: [specs/001-repoguide-breakdown/spec.md](spec.md)
**Input**: Feature specification for the RepoGuide repository breakdown tool.

## Summary
RepoGuide is a single-server Flask application that provides beginner-friendly breakdowns of GitHub repositories. It uses the GitHub REST API for raw metadata and the Gemini Flash API to generate human-readable summaries and contribution guides. The frontend uses Tailwind CSS v4 and DaisyUI via CDN to ensure zero build steps and high accessibility.

## Technical Context

**Language/Version**: Python 3.12
**Primary Dependencies**: Flask, requests, google-generativeai
**Storage**: N/A (Stateless, live fetching)
**Testing**: pytest
**Target Platform**: Web (Any modern browser), Linux/macOS server
**Project Type**: Web Service
**Performance Goals**: End-to-end analysis in under 10 seconds.
**Constraints**: No database, no backend queues, mobile-friendly UI.
**Scale/Scope**: Initial MVP focusing on public repositories only.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Principle I: Beginner-First Clarity**: ✅ (Design ensures AI prompts prioritize plain English and actionable steps).
- **Principle II: Free and Live Data Only**: ✅ (No database or persistent storage planned; all data fetched live).
- **Principle III: Single-Server Simplicity**: ✅ (Monolithic Flask architecture chosen).
- **Principle IV: Minimal Stack Discipline**: ✅ (Tailwind CSS v4 and DaisyUI via CDN; no build step).
- **Principle V: Speed and Accessibility**: ✅ (Mobile-friendly layout and optimized external API calls).

## Project Structure

### Documentation (this feature)

```text
specs/001-repoguide-breakdown/
├── plan.md              # This file
├── research.md          # Technology decisions and integration research
├── data-model.md        # Analysis result structure and validation
├── quickstart.md        # Setup and developer orientation
├── contracts/
│   └── api-contract.md  # POST /analyze request/response schema
└── tasks.md             # Generated implementation tasks
```

### Source Code (repository root)

```text
src/
├── app.py               # Flask application and main routes
├── services/
│   ├── github_service.py # GitHub REST API interaction logic
│   └── ai_service.py     # Gemini Flash API interaction logic
└── templates/
    └── index.html       # Single page UI (Tailwind + DaisyUI)

tests/
├── integration/
│   └── test_api.py      # Integration tests for /analyze endpoint
└── unit/
    ├── test_github_service.py
    └── test_ai_service.py
```

**Structure Decision**: Option 1 (Single project) is used because the frontend and backend are tightly coupled within a single Flask server, as mandated by the constitution.

## Complexity Tracking

*No violations identified.*
