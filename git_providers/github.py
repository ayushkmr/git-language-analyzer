import requests
from .base import GitProvider

class GitHubProvider(GitProvider):
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.headers = {"Authorization": f"token {token}"} if token else {}

    def get_user_repositories(self, username):
        url = f"{self.api_url}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_repository_languages(self, username, repo):
        url = f"{self.api_url}/repos/{username}/{repo}/languages"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()