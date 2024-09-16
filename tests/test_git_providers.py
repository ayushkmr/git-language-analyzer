import unittest
from unittest.mock import patch, MagicMock
from src.git_providers.github import GitHubProvider
from src.git_providers.gitlab import GitLabProvider
from src.utils.exceptions import UserNotFoundError, ApiError, RateLimitError

class TestGitHubProvider(unittest.TestCase):
    def setUp(self):
        self.provider = GitHubProvider("https://api.github.com", "test_token")

    @patch('requests.get')
    def test_get_user_repositories_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get.return_value = mock_response

        repos = self.provider.get_user_repositories("testuser")
        self.assertEqual(repos, ["repo1", "repo2"])

    @patch('requests.get')
    def test_get_user_repositories_user_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(UserNotFoundError) as context:
            self.provider.get_user_repositories("nonexistentuser")
        self.assertEqual(str(context.exception), "User 'nonexistentuser' not found on GitHub")

    @patch('requests.get')
    def test_get_repository_languages_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"Python": 1000, "JavaScript": 500}
        mock_get.return_value = mock_response

        languages = self.provider.get_repository_languages("testuser", "testrepo")
        self.assertEqual(languages, {"Python": 1000, "JavaScript": 500})

    @patch('requests.get')
    def test_rate_limit_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = "Rate limit exceeded"
        mock_get.return_value = mock_response

        with self.assertRaises(RateLimitError) as context:
            self.provider.get_user_repositories("testuser")
        self.assertEqual(str(context.exception), "API rate limit exceeded")

class TestGitLabProvider(unittest.TestCase):
    def setUp(self):
        self.provider = GitLabProvider("https://gitlab.com/api/v4", "test_token")

    @patch('requests.get')
    def test_get_user_repositories_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get.return_value = mock_response

        repos = self.provider.get_user_repositories("testuser")
        self.assertEqual(repos, ["repo1", "repo2"])

    @patch('requests.get')
    def test_get_user_repositories_user_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(UserNotFoundError) as context:
            self.provider.get_user_repositories("nonexistentuser")
        self.assertEqual(str(context.exception), "User 'nonexistentuser' not found on GitLab")

    @patch('requests.get')
    def test_get_repository_languages_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"Python": 60.0, "JavaScript": 40.0}
        mock_get.return_value = mock_response

        languages = self.provider.get_repository_languages("testuser", "testrepo")
        self.assertEqual(languages, {"Python": 60.0, "JavaScript": 40.0})

    @patch('requests.get')
    def test_api_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        with self.assertRaises(ApiError) as context:
            self.provider.get_user_repositories("testuser")
        self.assertEqual(str(context.exception), "API error: 500")

if __name__ == '__main__':
    unittest.main()