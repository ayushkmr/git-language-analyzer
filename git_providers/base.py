from abc import ABC, abstractmethod

class GitProvider(ABC):
    @abstractmethod
    def get_user_repositories(self, username):
        pass

    @abstractmethod
    def get_repository_languages(self, username, repo):
        pass