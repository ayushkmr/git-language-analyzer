import sys
from urllib.parse import urlparse
from git_providers.github import GitHubProvider
from git_providers.gitlab import GitLabProvider
from language_analyzer import LanguageAnalyzer
from utils.logger import Logger
from config_manager import ConfigManager

class GitLanguageAnalyzer:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.logger = Logger()
        self.providers = {
            'github.com': GitHubProvider,
            'gitlab.com': GitLabProvider
        }

    def configure_provider(self):
        print("\nConfigure Git Provider")
        print("Available providers:", ", ".join(self.providers.keys()))
        provider = input("Enter provider name: ").lower()
        
        if provider not in self.providers:
            print("Invalid provider")
            return

        api_url = input(f"Enter {provider} API URL: ")
        token = input(f"Enter {provider} access token: ")
        
        self.config_manager.set_provider_config(provider, api_url, token)
        print(f"{provider} configuration updated.")

    def analyze_profile(self, profile_url):
        try:
            parsed_url = urlparse(profile_url)
            domain = parsed_url.netloc
            
            if domain not in self.providers:
                raise ValueError(f"Unsupported Git provider: {domain}")
            
            config = self.config_manager.get_provider_config(domain.split('.')[0])
            provider = self.providers[domain](config['api_url'], config['token'])
            username = parsed_url.path.strip('/')
            
            analyzer = LanguageAnalyzer(provider)
            top_languages = analyzer.get_top_languages(username)
            
            self.print_results(username, top_languages)
        except Exception as e:
            self.logger.error(f"Error analyzing profile: {str(e)}")
            print(f"Error: {str(e)}")

    def print_results(self, username, top_languages):
        print(f"\nTop 5 languages for {username}:")
        for lang, percentage in top_languages.items():
            print(f"* {lang} ({percentage:.2f}%)")

def main_menu():
    analyzer = GitLanguageAnalyzer()
    
    while True:
        print("\nGit Language Analyzer")
        print("1. Configure Git Provider")
        print("2. Analyze Profile")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            analyzer.configure_provider()
        elif choice == '2':
            profile_url = input("Enter profile URL: ")
            analyzer.analyze_profile(profile_url)
        elif choice == '3':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()