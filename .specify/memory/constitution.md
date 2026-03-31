<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0 (MINOR: Materially expanded guidance with explicit rules and rationale)
- Modified principles:
  - I. Beginner-First Clarity: Added formal MUST rules and rationale.
  - II. Free and Live Data Only: Added formal MUST rules and rationale.
  - III. Single-Server Simplicity: Added formal MUST rules and rationale.
  - IV. Minimal Stack Discipline: Added formal MUST rules and rationale.
  - V. Speed and Accessibility: Added formal MUST rules and rationale.
- Added sections: Sync Impact Report, explicit Rules/Rationale for each Principle.
- Templates requiring updates (✅ updated):
  - .specify/templates/plan-template.md (alignment verified)
  - .specify/templates/spec-template.md (alignment verified)
  - .specify/templates/tasks-template.md (alignment verified)
- Follow-up TODOs: None.
-->

# RepoGuide Constitution

## Core Principles

### I. Beginner-First Clarity
RepoGuide must explain public GitHub repositories in plain English for beginners. 

- **Rules**: AI-generated summaries and first-contribution guides MUST prioritize clarity, accuracy, and actionable next steps over technical depth. Explanations MUST use plain English and avoid unnecessary jargon.
- **Rationale**: RepoGuide is specifically built for beginners who might be overwhelmed by technical complexity. Success is measured by how easily a newcomer can understand a project's purpose and how to start contributing.

### II. Free and Live Data Only
RepoGuide must run without paid services or persistent storage. 

- **Rules**: The application MUST NOT use a database, background queues, or paid third-party services. All repository metadata, languages, key files, and issue links MUST be fetched live from public sources (GitHub REST API) at request time.
- **Rationale**: This keeps the tool free to run, low-maintenance, and ensures that the information presented is always up-to-date with the live state of the repository.

### III. Single-Server Simplicity
The application must use one Python Flask server to serve both the frontend and REST API endpoints. 

- **Rules**: A single Flask server MUST handle both the UI (server-side rendering or static assets) and the API logic. The architecture SHOULD remain monolithic to simplify the mental model for beginners.
- **Rationale**: Reducing the number of moving parts (e.g., no separate frontend build step or microservices) makes it significantly easier for beginners to trace the request flow from the UI to the backend and external services.

### IV. Minimal Stack Discipline
The frontend must use HTML, Tailwind CSS v4, and DaisyUI via CDN with no build step. 

- **Rules**: AI text generation MUST use the Gemini Flash API free tier. Repository data MUST come from the public GitHub REST API without authentication requirements. Frontend dependencies MUST be loaded via CDN without a local build/transpilation step.
- **Rationale**: This stack ensures that anyone with a text editor can contribute to both the backend and frontend without needing to install complex toolchains like Node.js, npm, or build runners.

### V. Speed and Accessibility
The interface must be mobile-friendly and optimized for fast responses. 

- **Rules**: The UI MUST be responsive and mobile-friendly. End-to-end response time MUST be fast enough to feel "instant" (under 2 seconds where possible, accounting for AI generation). Code MUST be clean, readable, and lightly commented to help beginners understand non-obvious logic.
- **Rationale**: A fast, accessible tool encourages exploration. Clear, commented code ensures that the project itself serves as an example of the "beginner-friendly" principles it promotes.

## Technical Constraints

- **Backend**: Python Flask with REST API endpoints.
- **Frontend**: HTML enhanced with Tailwind CSS v4 and DaisyUI via CDN only.
- **AI**: Gemini Flash API (Free Tier).
- **Data Source**: Public GitHub REST API (No Auth).
- **Features**:
  - AI-generated plain English project summary.
  - Tech stack and language percentages.
  - Key files to read first.
  - Open `good first issue` links.
  - AI-generated step-by-step first contribution guide.

## Development Workflow

- **Principle-Led**: Every plan and specification must explicitly pass a "Constitution Check" against these principles.
- **Simple First**: Prefer straightforward implementations over abstractions. Complexity must be justified by an absolute necessity that cannot be resolved with a simpler approach.
- **Beginner Traceability**: Code organization must allow a beginner to trace a feature from the UI button click to the API call and the final data presentation.

## Governance

- **Amendments**: This constitution is the standard for RepoGuide decisions. Amendments require a documented rationale and must be reflected in the Sync Impact Report.
- **Versioning**: MAJOR (breaking changes to core principles), MINOR (new principles or expanded guidance), PATCH (clarifications and non-semantic refinements).
- **Compliance**: The `/speckit.plan` and `/speckit.tasks` commands MUST verify that all proposed work aligns with this document.

**Version**: 1.1.0 | **Ratified**: 2026-03-30 | **Last Amended**: 2026-03-30

