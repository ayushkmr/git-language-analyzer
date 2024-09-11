import requests
from .base import GitProvider

class GitLabProvider(GitProvider):
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.headers = {"Authorization": f"Bearer {token}"} if token else {}

    def get_user_repositories(self, username):
        url = f"{self.api_url}/users/{username}/projects"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_repository_languages(self, username, repo):
        url = f"{self.api_url}/projects/{username}%2F{repo}/languages"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()