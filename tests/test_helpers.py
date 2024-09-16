import unittest
from src.utils.helpers import parse_git_url, calculate_language_percentages
from src.utils.exceptions import ConfigurationError

class TestHelpers(unittest.TestCase):
    def test_parse_git_url_github(self):
        url = "https://github.com/username"
        domain, username = parse_git_url(url)
        self.assertEqual(domain, "github.com")
        self.assertEqual(username, "username")

    def test_parse_git_url_gitlab(self):
        url = "https://gitlab.com/username"
        domain, username = parse_git_url(url)
        self.assertEqual(domain, "gitlab.com")
        self.assertEqual(username, "username")

    def test_parse_git_url_invalid(self):
        url = "https://invalid.com"
        with self.assertRaises(ConfigurationError):
            parse_git_url(url)

    def test_calculate_language_percentages(self):
        languages = {
            "Python": 1000,
            "JavaScript": 500,
            "HTML": 250
        }
        percentages = calculate_language_percentages(languages)
        self.assertAlmostEqual(percentages["Python"], 57.14, places=2)
        self.assertAlmostEqual(percentages["JavaScript"], 28.57, places=2)
        self.assertAlmostEqual(percentages["HTML"], 14.29, places=2)

if __name__ == '__main__':
    unittest.main()