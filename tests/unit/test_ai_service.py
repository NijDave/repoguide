import pytest
from src.services.ai_service import generate_summary

def test_generate_summary_success(mocker):
    mock_model = mocker.Mock()
    mock_response = mocker.Mock()
    mock_response.text = "This is a plain English summary."
    mock_model.generate_content.return_value = mock_response
    
    metadata = {
        "owner": "psf",
        "repo": "requests",
        "description": "Python HTTP for Humans."
    }
    
    summary = generate_summary(mock_model, metadata)
    assert summary == "This is a plain English summary."
    mock_model.generate_content.assert_called_once()

def test_generate_contribution_guide_success(mocker):
    from src.services.ai_service import generate_contribution_guide
    mock_model = mocker.Mock()
    mock_response = mocker.Mock()
    mock_response.text = "1. Fork repo. 2. Fix issues."
    mock_model.generate_content.return_value = mock_response
    
    metadata = {"owner": "psf", "repo": "requests"}
    files = [{"name": "CONTRIBUTING.md"}]
    
    guide = generate_contribution_guide(mock_model, metadata, files)
    assert "Fork repo" in guide
    assert mock_model.generate_content.called
