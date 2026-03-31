# Research: RepoGuide Core Breakdown

## Decision: Python Flask with `google-generativeai` and `requests`
- **Rationale**: Flask provides a lightweight, single-server architecture as required by the constitution. The `google-generativeai` library is the official Python client for Gemini. `requests` is the standard for calling the GitHub REST API.
- **Alternatives considered**: FastAPI (more complex for beginners), Django (too heavy, requires DB).

## Decision: GitHub REST API (No Auth)
- **Rationale**: The specification requires no authentication for initial use. We will use public endpoints to fetch repository metadata, languages, and issues.
- **Endpoints**:
  - `GET /repos/{owner}/{repo}`: General metadata and description.
  - `GET /repos/{owner}/{repo}/languages`: Tech stack breakdown.
  - `GET /repos/{owner}/{repo}/issues?labels=good+first+issue&state=open`: Labeled issues.
  - `GET /repos/{owner}/{repo}/contents`: Identify key files like README, CONTRIBUTING.

## Decision: Gemini Flash 1.5 API (Free Tier)
- **Rationale**: Cost-effective and fast for generating summaries and guides.
- **Prompt Strategy**: Prompts will be engineered to enforce "Plain English" and "Beginner-Friendly" output as per Principle I.

## Decision: Tailwind CSS v4 + DaisyUI via CDN
- **Rationale**: Meets Principle IV (No build step). Tailwind 4 includes a standalone browser engine that processes directives without a CLI. DaisyUI adds ready-to-use components.
- **Implementation**: Single `<script src="https://unpkg.com/@tailwindcss/browser@4"></script>` and `<link href="https://cdn.jsdelivr.net/npm/daisyui@latest/dist/full.css" rel="stylesheet">`.
