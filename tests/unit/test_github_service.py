import pytest
from src.services.github_service import GitHubService

def test_get_repo_metadata_success(mocker):
    service = GitHubService()
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "full_name": "psf/requests",
        "description": "Python HTTP for Humans.",
        "owner": {"login": "psf"},
        "name": "requests"
    }
    mocker.patch("requests.get", return_value=mock_response)
    
    metadata = service.get_repo_metadata("psf", "requests")
    assert metadata["owner"] == "psf"
    assert metadata["repo"] == "requests"
    assert "Python HTTP for Humans" in metadata["description"]

def test_get_repo_metadata_not_found(mocker):
    service = GitHubService()
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch("requests.get", return_value=mock_response)
    
    with pytest.raises(ValueError, match="Repository not found"):
        service.get_repo_metadata("nonexistent", "repo")

def test_get_repo_languages_success(mocker):
    service = GitHubService()
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"Python": 1000, "Shell": 100}
    mocker.patch("requests.get", return_value=mock_response)
    
    languages = service.get_repo_languages("psf", "requests")
    assert len(languages) == 2
    assert languages[0]["name"] == "Python"
    assert languages[0]["percentage"] == 90.9
    assert languages[1]["name"] == "Shell"
    assert languages[1]["percentage"] == 9.1

def test_get_key_files_success(mocker):
    service = GitHubService()
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"name": "README.md", "html_url": "url1", "type": "file"},
        {"name": "CONTRIBUTING.md", "html_url": "url2", "type": "file"},
        {"name": "src", "html_url": "url3", "type": "dir"}
    ]
    mocker.patch("requests.get", return_value=mock_response)
    
    key_files = service.get_key_files("psf", "requests")
    assert len(key_files) == 2
    assert key_files[0]["name"] == "README.md"
    assert key_files[1]["name"] == "CONTRIBUTING.md"

def test_get_good_first_issues_success(mocker):
    service = GitHubService()
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"title": "Fix typo", "html_url": "url1"},
        {"title": "Update docs", "html_url": "url2"}
    ]
    mocker.patch("requests.get", return_value=mock_response)
    
    issues = service.get_good_first_issues("psf", "requests")
    assert len(issues) == 2
    assert issues[0]["title"] == "Fix typo"
    assert issues[1]["url"] == "url2"
