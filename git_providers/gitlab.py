import requests
from .base import GitProvider
from utils.exceptions import UserNotFoundError

class GitLabProvider(GitProvider):
    def __init__(self, api_url, token):
        super().__init__(api_url, token)
        self.headers = {"Authorization": f"Bearer {token}"} if token else {}

    def get_user_repositories(self, username):
        url = f"{self.api_url}/users/{username}/projects"
        self.log_api_call("GET", url)
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 404:
            raise UserNotFoundError(f"User '{username}' not found on GitLab")
        
        data = self.handle_response(response)
        return [repo['name'] for repo in data]

    def get_repository_languages(self, username, repo):
        url = f"{self.api_url}/projects/{username}%2F{repo}/languages"
        self.log_api_call("GET", url)
        response = requests.get(url, headers=self.headers)
        return self.handle_response(response)
