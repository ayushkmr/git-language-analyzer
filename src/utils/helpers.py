from urllib.parse import urlparse
from src.utils.exceptions import ConfigurationError

def parse_git_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    username = parsed_url.path.strip('/').split('/')[0]
    
    if not domain or not username:
        raise ConfigurationError("Invalid Git profile URL")
    
    return domain, username

def calculate_language_percentages(languages):
    total = sum(languages.values())
    return {lang: (count / total) * 100 for lang, count in languages.items()}