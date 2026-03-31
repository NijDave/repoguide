# RepoGuide

RepoGuide is a beginner-friendly tool that provides instant breakdowns of GitHub repositories. It uses AI to generate plain-English summaries and step-by-step contribution guides, helping new developers understand and start contributing to projects faster.

## Features

- **AI Project Summary**: Understand what a project does in seconds without jargon.
- **Tech Stack Insights**: See programming languages used with percentage breakdowns.
- **Key Files**: Quick links to README, CONTRIBUTING, and LICENSE files.
- **Contribution Path**: AI-generated step-by-step guide tailored to the repository.
- **Good First Issues**: Direct links to open issues labeled for beginners.

## Tech Stack

- **Backend**: Python 3.12, Flask
- **AI**: Gemini 1.5 Flash (google-generativeai)
- **Frontend**: Tailwind CSS v4, DaisyUI (via CDN)
- **API**: GitHub REST API

## Getting Started

### Prerequisites

- Python 3.12+
- Gemini API Key (get one at [Google AI Studio](https://aistudio.google.com/))

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repoguide.git
   cd repoguide
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### Running the App

```bash
python3 src/app.py
```

The application will be available at `http://127.0.0.1:5000`.

## Testing

Run tests using pytest:
```bash
PYTHONPATH=. venv/bin/python3 -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
