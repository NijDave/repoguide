import requests

class GitHubService:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "RepoGuide-App"
        }

    def get_repo_metadata(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return {
                "owner": data["owner"]["login"],
                "repo": data["name"],
                "description": data.get("description", "No description provided.")
            }
        elif response.status_code == 404:
            raise ValueError("Repository not found.")
        else:
            raise Exception(f"GitHub API error: {response.status_code}")

    def get_repo_languages(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/languages"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            total_bytes = sum(data.values())
            if total_bytes == 0:
                return []
            
            languages = []
            for name, bytes_count in data.items():
                percentage = round((bytes_count / total_bytes) * 100, 1)
                languages.append({"name": name, "percentage": percentage})
            
            # Sort by percentage descending
            languages.sort(key=lambda x: x["percentage"], reverse=True)
            return languages
        return []

    def get_key_files(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/contents"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            contents = response.json()
            key_names = ["README", "CONTRIBUTING", "LICENSE", "SECURITY"]
            key_files = []
            
            for item in contents:
                if item["type"] == "file":
                    name_upper = item["name"].upper()
                    if any(key in name_upper for key in key_names):
                        key_files.append({
                            "name": item["name"],
                            "url": item["html_url"]
                        })
            return key_files
        return []

    def get_good_first_issues(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        params = {
            "labels": "good first issue",
            "state": "open",
            "per_page": 5
        }
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            issues = response.json()
            return [{
                "title": issue["title"],
                "url": issue["html_url"]
            } for issue in issues]
        return []
