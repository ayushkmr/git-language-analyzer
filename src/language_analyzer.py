from collections import Counter
from src.utils.logger import get_logger
from src.utils.helpers import calculate_language_percentages

class LanguageAnalyzer:
    def __init__(self, git_provider):
        self.git_provider = git_provider
        self.logger = get_logger(self.__class__.__name__)

    def get_top_languages(self, username, limit=5):
        self.logger.info(f"Analyzing top languages for user: {username}")
        repositories = self.git_provider.get_user_repositories(username)
        
        if not repositories:
            self.logger.warning(f"No repositories found for user: {username}")
            return {}

        all_languages = Counter()

        for repo in repositories:
            self.logger.debug(f"Fetching languages for repository: {repo}")
            languages = self.git_provider.get_repository_languages(username, repo)
            all_languages.update(languages)

        top_languages = dict(all_languages.most_common(limit))
        percentages = calculate_language_percentages(top_languages)

        self.logger.info(f"Top {limit} languages analyzed for user: {username}")
        return percentages