import re
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from src.services.github_service import GitHubService
from src.services.ai_service import init_ai

# Load environment variables from .env if it exists
load_dotenv()

app = Flask(__name__)

# Initialize services
try:
    ai_model = init_ai()
    github_service = GitHubService()
except Exception as e:
    print(f"Error initializing services: {e}")
    ai_model = None
    github_service = None

# Regex for valid public GitHub repository URL
GITHUB_URL_PATTERN = re.compile(r'^https?://github\.com/([^/]+)/([^/]+)/?$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if not ai_model or not github_service:
        return jsonify({
            "status": "error",
            "message": "System services are not properly initialized."
        }), 500
    
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({
            "status": "error",
            "message": "GitHub repository URL is required."
        }), 400
    
    url = data['url'].strip().rstrip('/')
    
    match = GITHUB_URL_PATTERN.match(url)
    if not match:
        return jsonify({
            "status": "error", 
            "message": "Please provide a valid public GitHub repository URL (e.g., https://github.com/owner/repo)."
        }), 400
    
    owner, repo = match.groups()

    try:
        # US1: Summary
        metadata = github_service.get_repo_metadata(owner, repo)
        from src.services.ai_service import generate_summary, generate_contribution_guide
        summary = generate_summary(ai_model, metadata)
        
        # US2: Tech Stack & Key Files
        languages = github_service.get_repo_languages(owner, repo) or []
        key_files = github_service.get_key_files(owner, repo) or []
        
        # US3: Issues & Guide
        issues = github_service.get_good_first_issues(owner, repo) or []
        guide = generate_contribution_guide(ai_model, metadata, key_files) or ""

        return jsonify({
            "status": "success",
            "data": {
                "owner": owner,
                "repo": repo,
                "summary": summary,
                "languages": languages,
                "key_files": key_files,
                "good_first_issues": issues,
                "contribution_guide": guide
            }
        })
    except ValueError as ve:
        return jsonify({"status": "error", "message": str(ve)}), 404
    except Exception as e:
        print(f"Error during analysis: {e}")
        return jsonify({"status": "error", "message": "An error occurred during repository analysis."}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"status": "error", "message": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
