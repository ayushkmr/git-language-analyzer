import unittest
from unittest.mock import MagicMock
from src.language_analyzer import LanguageAnalyzer
from src.utils.helpers import calculate_language_percentages

class TestLanguageAnalyzer(unittest.TestCase):
    def setUp(self):
        self.mock_provider = MagicMock()
        self.analyzer = LanguageAnalyzer(self.mock_provider)

    def test_get_top_languages_success(self):
        self.mock_provider.get_user_repositories.return_value = ["repo1", "repo2"]
        self.mock_provider.get_repository_languages.side_effect = [
            {"Python": 1000, "JavaScript": 500},
            {"Python": 800, "Java": 700}
        ]

        top_languages = self.analyzer.get_top_languages("testuser")
        expected_result = {
            "Python": 60.0,
            "JavaScript": 16.67,
            "Java": 23.33
        }

        self.assertEqual(len(top_languages), 3)
        for lang, percentage in top_languages.items():
            self.assertAlmostEqual(percentage, expected_result[lang], places=2)

    def test_get_top_languages_no_repositories(self):
        self.mock_provider.get_user_repositories.return_value = []

        top_languages = self.analyzer.get_top_languages("testuser")
        self.assertEqual(top_languages, {})

    def test_get_top_languages_limit(self):
        self.mock_provider.get_user_repositories.return_value = ["repo1", "repo2"]
        self.mock_provider.get_repository_languages.side_effect = [
            {"Python": 1000, "JavaScript": 500, "Java": 300},
            {"Python": 800, "C++": 600, "Ruby": 400}
        ]

        top_languages = self.analyzer.get_top_languages("testuser", limit=2)
        self.assertEqual(len(top_languages), 2)
        self.assertIn("Python", top_languages)
        self.assertTrue("JavaScript" in top_languages or "C++" in top_languages)

    def test_calculate_language_percentages(self):
        languages = {
            "Python": 1000,
            "JavaScript": 500,
            "Java": 500
        }
        percentages = calculate_language_percentages(languages)
        expected_result = {
            "Python": 50.0,
            "JavaScript": 25.0,
            "Java": 25.0
        }
        self.assertEqual(percentages, expected_result)

if __name__ == '__main__':
    unittest.main()