import json
import os
from src.utils.logger import get_logger
from src.utils.exceptions import ConfigurationError

class ConfigManager:
    def __init__(self, config_path='config/config.json'):
        self.config_path = config_path
        self.logger = get_logger(self.__class__.__name__)
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            self.logger.info("Configuration loaded successfully")
            return config
        except FileNotFoundError:
            self.logger.error(f"Configuration file not found: {self.config_path}")
            raise ConfigurationError(f"Configuration file not found: {self.config_path}")
        except json.JSONDecodeError:
            self.logger.error(f"Invalid JSON in configuration file: {self.config_path}")
            raise ConfigurationError(f"Invalid JSON in configuration file: {self.config_path}")

    def save_config(self):
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
        self.logger.info("Configuration saved successfully")

    def get_provider_config(self, provider):
        if provider not in self.config:
            self.logger.error(f"Provider not found in configuration: {provider}")
            raise ConfigurationError(f"Provider not found in configuration: {provider}")
        return self.config[provider]

    def set_provider_config(self, provider, api_url, token):
        self.config[provider] = {"api_url": api_url, "token": token}
        self.save_config()
        self.logger.info(f"Configuration updated for provider: {provider}")

    def get_providers(self):
        return list(self.config.keys())