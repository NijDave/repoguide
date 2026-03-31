import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_analyze_endpoint_missing_url(client, mocker):
    # Mock services to avoid init errors
    mocker.patch("src.app.ai_model", mocker.Mock())
    mocker.patch("src.app.github_service", mocker.Mock())
    
    response = client.post('/analyze', json={})
    assert response.status_code == 400
    assert response.get_json()["message"] == "GitHub repository URL is required."

def test_analyze_endpoint_success(client, mocker):
    # Mock services
    mock_github = mocker.Mock()
    mock_github.get_repo_metadata.return_value = {
        "owner": "psf", "repo": "requests", "description": "Python HTTP for Humans."
    }
    mock_github.get_repo_languages.return_value = [{"name": "Python", "percentage": 100.0}]
    mock_github.get_key_files.return_value = [{"name": "README.md", "url": "https://github.com/psf/requests/blob/main/README.md"}]
    mock_github.get_good_first_issues.return_value = []
    
    mocker.patch("src.app.github_service", mock_github)
    mocker.patch("src.app.ai_model", mocker.Mock())
    
    # Correct mock targets for functions imported inside analyze()
    mocker.patch("src.services.ai_service.generate_summary", return_value="AI Summary")
    mocker.patch("src.services.ai_service.generate_contribution_guide", return_value="AI Guide")
    
    response = client.post('/analyze', json={"url": "https://github.com/psf/requests"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "data" in data
    assert data["data"]["summary"] == "AI Summary"
    assert len(data["data"]["languages"]) > 0
    assert data["data"]["languages"][0]["name"] == "Python"
    assert len(data["data"]["key_files"]) > 0
    assert data["data"]["key_files"][0]["name"] == "README.md"
    assert data["data"]["contribution_guide"] == "AI Guide"
