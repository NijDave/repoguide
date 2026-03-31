# Data Model: RepoGuide Core Breakdown

## RepositoryAnalysis (Entity)

| Field | Type | Description |
|-------|------|-------------|
| owner | String | GitHub username or organization |
| repo | String | Name of the repository |
| summary | String | Plain English summary (AI generated) |
| languages | List[Language] | Tech stack breakdown |
| key_files | List[FileLink] | List of essential files for beginners |
| good_first_issues | List[IssueLink] | Issues labeled "good first issue" |
| contribution_guide | String | Step-by-step contribution guide (AI generated) |

## Supporting Types

### Language
- `name`: String
- `percentage`: Float

### FileLink
- `name`: String
- `url`: String

### IssueLink
- `title`: String
- `url`: String

## Validation Rules
- **URL Validation**: Input must match a public GitHub repository pattern (`https://github.com/OWNER/REPO`).
- **Data Completeness**: All fields in `RepositoryAnalysis` must be populated for a successful response.
- **AI Constraints**: Summaries and guides must not exceed 500 words each to ensure clarity and speed.
