from abc import ABC, abstractmethod
from src.utils.logger import get_logger
from src.utils.exceptions import ApiError, RateLimitError

class GitProvider(ABC):
    def __init__(self, api_url, token):
        self.api_url = api_url
        self.token = token
        self.logger = get_logger(self.__class__.__name__)

    @abstractmethod
    def get_user_repositories(self, username):
        pass

    @abstractmethod
    def get_repository_languages(self, username, repo):
        pass

    def handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            self.logger.error(f"Rate limit exceeded: {response.text}")
            raise RateLimitError("API rate limit exceeded")
        else:
            self.logger.error(f"API error: {response.status_code} - {response.text}")
            raise ApiError(f"API error: {response.status_code}")

    def log_api_call(self, method, url):
        self.logger.info(f"API call: {method} {url}")