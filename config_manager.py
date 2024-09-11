import json
import os

class ConfigManager:
    def __init__(self, config_path='config/config.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self):
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)

    def get_provider_config(self, provider):
        return self.config.get(provider, {})

    def set_provider_config(self, provider, api_url, token):
        self.config[provider] = {"api_url": api_url, "token": token}
        self.save_config()

    def get_providers(self):
        return list(self.config.keys())