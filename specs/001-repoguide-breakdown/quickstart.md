# Quickstart: RepoGuide

## Prerequisites
- Python 3.12+
- Gemini API Key (obtain from [Google AI Studio](https://aistudio.google.com/))

## Setup
1. Clone the repository and enter the project directory.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root:
   ```env
   GEMINI_API_KEY='your-api-key-here'
   ```

## Running the Application
```bash
python3 src/app.py
```
The application will be available at `http://127.0.0.1:5000`.

## Running Tests
To run all tests:
```bash
PYTHONPATH=. venv/bin/python3 -m pytest
```

## Testing the Analysis via CLI
You can test the analysis endpoint using `curl`:
```bash
curl -X POST http://127.0.0.1:5000/analyze \
     -H "Content-Type: application/json" \
     -d '{"url": "https://github.com/psf/requests"}'
```
