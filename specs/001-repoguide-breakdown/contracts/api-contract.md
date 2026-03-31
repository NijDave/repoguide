# API Contract: RepoGuide Core Breakdown

## Endpoint: POST /analyze

**Description**: Analyzes a public GitHub repository and returns a beginner-friendly breakdown.

### Request Body (JSON)
```json
{
  "url": "https://github.com/OWNER/REPO"
}
```

### Response Body (JSON - 200 OK)
```json
{
  "status": "success",
  "data": {
    "owner": "psf",
    "repo": "requests",
    "summary": "Requests is an elegant and simple HTTP library for Python, built for human beings.",
    "languages": [
      { "name": "Python", "percentage": 99.1 },
      { "name": "Other", "percentage": 0.9 }
    ],
    "key_files": [
      { "name": "README.md", "url": "https://github.com/psf/requests/blob/main/README.md" },
      { "name": "CONTRIBUTING.md", "url": "https://github.com/psf/requests/blob/main/CONTRIBUTING.md" }
    ],
    "good_first_issues": [
      { "name": "Docs: Fix typo in quickstart", "url": "https://github.com/psf/requests/issues/123" }
    ],
    "contribution_guide": "1. Fork the repository. 2. Clone to your local machine. 3. Install dev dependencies..."
  }
}
```

### Response Body (JSON - 400 Bad Request)
```json
{
  "status": "error",
  "message": "Invalid GitHub repository URL."
}
```

### Response Body (JSON - 500 Server Error)
```json
{
  "status": "error",
  "message": "Failed to fetch repository data from GitHub."
}
```
