# Feature Specification: RepoGuide Core Breakdown

**Feature Branch**: `001-repoguide-breakdown`  
**Created**: 2026-03-30  
**Status**: Draft  
**Input**: User description: "RepoGuide is a Flask web app where users paste a GitHub repo URL and get a beginner-friendly breakdown. Features: AI plain English summary, tech stack with language percentages, key files to read first, good first issues with links, and step by step contribution guide. Single page app, no login needed, no database, results shown on same page after form submit."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Repository Breakdown Request (Priority: P1)

As a beginner developer, I want to paste a GitHub URL into a simple input field so that I can instantly see a plain-English explanation of what the project does without reading complex documentation.

**Why this priority**: This is the core value proposition. Without the ability to submit a URL and get a summary, the app has no purpose.

**Independent Test**: Can be tested by navigating to the home page, entering a valid public GitHub URL, and verifying that a summary is displayed on the same page.

**Acceptance Scenarios**:

1. **Given** the user is on the RepoGuide home page, **When** they paste `https://github.com/psf/requests` and click submit, **Then** they should see an AI-generated summary of the Requests library on the same page.
2. **Given** the user is on the RepoGuide home page, **When** they enter an invalid URL, **Then** they should see a clear error message explaining that a valid GitHub URL is required.

---

### User Story 2 - Tech Stack and File Insights (Priority: P2)

As a developer looking to contribute, I want to see the programming languages used and the most important files so that I know if I have the right skills and where to start looking at the code.

**Why this priority**: Helps users decide if the project is a good match for their current technical knowledge.

**Independent Test**: Can be tested by submitting a URL and verifying the presence of a "Tech Stack" section with percentages and a "Key Files" list.

**Acceptance Scenarios**:

1. **Given** a successful repository fetch, **When** the results are displayed, **Then** the user should see a list or chart of languages (e.g., Python 95%, Shell 5%).
2. **Given** a successful repository fetch, **When** the results are displayed, **Then** the user should see links to essential files like README, CONTRIBUTING, or LICENSE if they exist.

---

### User Story 3 - Contribution Path (Priority: P3)

As a first-time contributor, I want to see "good first issues" and a step-by-step guide so that I have a clear, non-intimidating path to making my first pull request.

**Why this priority**: Converts interest into action, fulfilling the "beginner-friendly" mission of the tool.

**Independent Test**: Can be tested by submitting a repository known to have "good first issue" labels and verifying the issues are linked and a guide is generated.

**Acceptance Scenarios**:

1. **Given** a repository with "good first issue" labels, **When** the breakdown is shown, **Then** those issues should be listed with direct links to GitHub.
2. **Given** a successful fetch, **When** the results are displayed, **Then** a "How to Contribute" section should provide a step-by-step guide tailored to that specific repository.

---

### Edge Cases

- **Private Repositories**: What happens when a user submits a private URL? (System should explain it only supports public repositories).
- **Empty/Non-GitHub URLs**: How does the system handle strings that aren't URLs or point to other sites? (Show validation error).
- **Repositories with no "good first issues"**: What is shown if no labeled issues are found? (Inform the user that no specific beginner issues were found but suggest general next steps).
- **API Rate Limits**: How does the system handle being rate-limited by GitHub or the AI service? (Display a "try again later" message instead of crashing).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a single-page interface with a prominent URL input field.
- **FR-002**: System MUST validate that the input is a valid public GitHub repository URL.
- **FR-003**: System MUST fetch repository metadata, languages, and issues live from the GitHub REST API.
- **FR-004**: System MUST generate a plain-English project summary using the Gemini Flash API.
- **FR-005**: System MUST display the "Tech Stack" as a list of languages with their respective percentage of the codebase.
- **FR-006**: System MUST identify and list links to key files (README, CONTRIBUTING, etc.).
- **FR-007**: System MUST filter and display open issues labeled as "good first issue".
- **FR-008**: System MUST generate a custom step-by-step contribution guide via AI based on the repository structure.
- **FR-009**: System MUST display all results on the same page without requiring a login or page reload.
- **FR-010**: System MUST NOT store any user or repository data in a persistent database.

### Key Entities

- **Repository**: Represents the GitHub project being analyzed (Attributes: owner, name, description, URL, primary language).
- **AnalysisResult**: The compiled breakdown for the user (Attributes: AI summary, language list, key file list, issue list, contribution guide).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can get a complete breakdown of any public repository in under 10 seconds (end-to-end).
- **SC-002**: 100% of valid public GitHub URLs result in a displayed summary or a meaningful error message.
- **SC-003**: The interface is fully usable on mobile devices with no horizontal scrolling required for primary content.
- **SC-004**: Users can transition from pasting a URL to viewing the "How to Contribute" guide with zero intermediate clicks (other than "Submit").

## Assumptions

- **Internet Connectivity**: Users have a stable internet connection to reach the Flask server and for the server to reach GitHub/Gemini.
- **Public API Availability**: The GitHub and Gemini APIs are operational and their free tiers provide sufficient rate limits for initial usage.
- **No Authentication Needed**: The tool only works for public information that does not require a GitHub personal access token for basic REST API access.
