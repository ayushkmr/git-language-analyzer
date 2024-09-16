import unittest
import tempfile
import json
import os
from src.config_manager import ConfigManager
from src.utils.exceptions import ConfigurationError

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.config_path = os.path.join(self.temp_dir, 'test_config.json')
        self.test_config = {
            "github": {
                "api_url": "https://api.github.com",
                "token": "test_token"
            }
        }
        with open(self.config_path, 'w') as f:
            json.dump(self.test_config, f)
        
        self.config_manager = ConfigManager(self.config_path)

    def tearDown(self):
        os.remove(self.config_path)
        os.rmdir(self.temp_dir)

    def test_load_config(self):
        self.assertEqual(self.config_manager.config, self.test_config)

    def test_get_provider_config(self):
        github_config = self.config_manager.get_provider_config('github')
        self.assertEqual(github_config, self.test_config['github'])

    def test_get_provider_config_error(self):
        with self.assertRaises(ConfigurationError) as context:
            self.config_manager.get_provider_config('nonexistent')
        self.assertEqual(str(context.exception), "Provider not found in configuration: nonexistent")

    def test_set_provider_config(self):
        self.config_manager.set_provider_config('gitlab', 'https://gitlab.com/api/v4', 'new_token')
        self.assertIn('gitlab', self.config_manager.config)
        self.assertEqual(self.config_manager.config['gitlab']['api_url'], 'https://gitlab.com/api/v4')
        self.assertEqual(self.config_manager.config['gitlab']['token'], 'new_token')

    def test_get_providers(self):
        providers = self.config_manager.get_providers()
        self.assertEqual(providers, ['github'])

if __name__ == '__main__':
    unittest.main()