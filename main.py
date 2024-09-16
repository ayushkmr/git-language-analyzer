import sys
from git_providers.github import GitHubProvider
from git_providers.gitlab import GitLabProvider
from language_analyzer import LanguageAnalyzer
from config_manager import ConfigManager
from utils.logger import get_logger
from utils.exceptions import GitLanguageAnalyzerError, UserNotFoundError
from utils.helpers import parse_git_url

class GitLanguageAnalyzer:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.logger = get_logger(self.__class__.__name__)
        self.providers = {
            'github.com': GitHubProvider,
            'gitlab.com': GitLabProvider
        }

    def configure_provider(self):
        self.logger.info("Configuring Git provider")
        print("\nConfigure Git Provider")
        print("Available providers:", ", ".join(self.providers.keys()))
        provider = input("Enter provider name: ").lower()
        
        if provider not in self.providers:
            self.logger.warning(f"Invalid provider selected: {provider}")
            print("Invalid provider")
            return

        api_url = input(f"Enter {provider} API URL: ")
        token = input(f"Enter {provider} access token: ")
        
        self.config_manager.set_provider_config(provider, api_url, token)
        self.logger.info(f"Provider {provider} configured successfully")
        print(f"{provider} configuration updated.")

    def analyze_profile(self, profile_url):
        self.logger.info(f"Analyzing profile: {profile_url}")
        try:
            domain, username = parse_git_url(profile_url)
            
            if domain not in self.providers:
                raise GitLanguageAnalyzerError(f"Unsupported Git provider: {domain}")
            
            config = self.config_manager.get_provider_config(domain.split('.')[0])
            provider = self.providers[domain](config['api_url'], config['token'])
            
            analyzer = LanguageAnalyzer(provider)
            top_languages = analyzer.get_top_languages(username)
            
            self.print_results(username, top_languages)
        except UserNotFoundError as e:
            self.logger.error(f"User not found: {str(e)}")
            print(f"Error: {str(e)}")
        except GitLanguageAnalyzerError as e:
            self.logger.error(f"Error analyzing profile: {str(e)}")
            print(f"Error: {str(e)}")
        except Exception as e:
            self.logger.exception(f"Unexpected error: {str(e)}")
            print(f"An unexpected error occurred. Please check the logs for details.")

    def print_results(self, username, top_languages):
        if not top_languages:
            print(f"\nNo language data found for {username}")
            return

        print(f"\nTop 5 languages for {username}:")
        for lang, percentage in top_languages.items():
            print(f"* {lang} ({percentage:.2f}%)")

def main_menu():
    analyzer = GitLanguageAnalyzer()
    logger = get_logger("main")
    
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
            logger.info("Exiting application")
            print("Exiting...")
            sys.exit(0)
        else:
            logger.warning(f"Invalid menu choice: {choice}")
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()