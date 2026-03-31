# Tasks: RepoGuide Core Breakdown

**Input**: Design documents from `/specs/001-repoguide-breakdown/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure: `src/services/`, `src/templates/`, `tests/unit/`, `tests/integration/`
- [x] T002 Initialize Python project with `venv` and install `flask`, `requests`, `google-generativeai`, `pytest`
- [x] T003 [P] Configure `.gitignore` for Python and environment variables
- [x] T004 [P] Create `requirements.txt` with pinned versions for project dependencies

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [x] T005 [P] Implement environment variable loading for `GEMINI_API_KEY` in `src/app.py`
- [x] T006 [P] Initialize Flask application and base routing structure in `src/app.py`
- [x] T007 Setup global error handling and JSON response utility in `src/app.py`
- [x] T008 [P] Initialize Gemini AI client in `src/services/ai_service.py`
- [x] T009 [P] Initialize GitHub API request helper in `src/services/github_service.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Repository Breakdown Request (Priority: P1) 🎯 MVP

**Goal**: Allow users to submit a GitHub URL and receive a plain-English AI summary.

**Independent Test**: Submit a valid URL to `/analyze` and verify the `summary` field is populated in the JSON response.

### Tests for User Story 1

- [x] T010 [P] [US1] Unit test for GitHub metadata fetching in `tests/unit/test_github_service.py`
- [x] T011 [P] [US1] Unit test for Gemini summary generation in `tests/unit/test_ai_service.py`
- [x] T012 [US1] Integration test for `POST /analyze` basic summary flow in `tests/integration/test_api.py`

### Implementation for User Story 1

- [x] T013 [P] [US1] Implement `get_repo_metadata(url)` in `src/services/github_service.py`
- [x] T014 [P] [US1] Implement `generate_summary(metadata)` in `src/services/ai_service.py`
- [x] T015 [US1] Implement `POST /analyze` endpoint in `src/app.py` to coordinate metadata fetch and summary generation
- [x] T016 [US1] Create basic `index.html` with URL input form and summary display area using Tailwind CSS v4 and DaisyUI

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Tech Stack and File Insights (Priority: P2)

**Goal**: Display language percentages and links to key repository files.

**Independent Test**: Submit a URL and verify `languages` and `key_files` are present and correctly formatted in the output.

### Tests for User Story 2

- [x] T017 [P] [US2] Unit test for GitHub languages fetching in `tests/unit/test_github_service.py`
- [x] T018 [P] [US2] Unit test for key file identification in `tests/unit/test_github_service.py`
- [x] T019 [US2] Integration test for `POST /analyze` including tech stack and files in `tests/integration/test_api.py`

### Implementation for User Story 2

- [x] T020 [P] [US2] Implement `get_repo_languages(owner, repo)` in `src/services/github_service.py`
- [x] T021 [P] [US2] Implement `get_key_files(owner, repo)` in `src/services/github_service.py` (checking for README, etc.)
- [x] T022 [US2] Update `POST /analyze` in `src/app.py` to include languages and key files in the result
- [x] T023 [US2] Update `index.html` to display the "Tech Stack" list and "Key Files" links

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Contribution Path (Priority: P3)

**Goal**: List "good first issues" and generate a step-by-step contribution guide.

**Independent Test**: Submit a repository with labeled issues and verify they are listed alongside an AI-generated guide.

### Tests for User Story 3

- [x] T024 [P] [US3] Unit test for "good first issue" fetching in `tests/unit/test_github_service.py`
- [x] T025 [P] [US3] Unit test for AI contribution guide generation in `tests/unit/test_ai_service.py`
- [x] T026 [US3] Integration test for `POST /analyze` full response in `tests/integration/test_api.py`

### Implementation for User Story 3

- [x] T027 [P] [US3] Implement `get_good_first_issues(owner, repo)` in `src/services/github_service.py`
- [x] T028 [P] [US3] Implement `generate_contribution_guide(metadata, files)` in `src/services/ai_service.py`
- [x] T029 [US3] Update `POST /analyze` in `src/app.py` to include issues and the contribution guide
- [x] T030 [US3] Update `index.html` to display "Good First Issues" and the "How to Contribute" guide

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and verification

- [x] T031 [P] Update `README.md` at repository root with usage instructions
- [x] T032 Add input validation for GitHub URLs (regex) in `src/app.py`
- [x] T033 Implement responsive UI refinements for mobile devices in `src/templates/index.html`
- [x] T034 [P] Final run of all tests and linting via `pytest` and `ruff check .`
- [x] T035 [P] Documentation updates in `quickstart.md` if any setup steps changed

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can proceed sequentially (P1 → P2 → P3) or in parallel where feasible
- **Polish (Final Phase)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Phase 2 - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Phase 2 - Independent of US1 but shares `github_service.py`
- **User Story 3 (P3)**: Can start after Phase 2 - Independent of US1/US2 but shares services

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Verify summary generation works end-to-end

### Incremental Delivery

1. Deploy Phase 3 (US1) as the initial functional prototype.
2. Incrementally add US2 (Tech Stack/Files) and US3 (Contribution Path) as functional enhancements.
3. Each story is verified against its own independent test criteria before merging.

---

## Parallel Example: User Story 1

```bash
# Implement GitHub and AI services in parallel
Task: "Implement get_repo_metadata(url) in src/services/github_service.py"
Task: "Implement generate_summary(metadata) in src/services/ai_service.py"

# Write tests while implementation is in progress
Task: "Unit test for GitHub metadata fetching in tests/unit/test_github_service.py"
Task: "Unit test for Gemini summary generation in tests/unit/test_ai_service.py"
```
