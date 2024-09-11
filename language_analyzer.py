from collections import Counter

class LanguageAnalyzer:
    def __init__(self, git_provider):
        self.git_provider = git_provider

    def get_top_languages(self, username, limit=5):
        repositories = self.git_provider.get_user_repositories(username)
        all_languages = Counter()

        for repo in repositories:
            repo_name = repo['name']
            languages = self.git_provider.get_repository_languages(username, repo_name)
            all_languages.update(languages)

        total_bytes = sum(all_languages.values())
        top_languages = {lang: (count / total_bytes) * 100 for lang, count in all_languages.most_common(limit)}

        return top_languages