class GitLanguageAnalyzerError(Exception):
    """Base exception for GitLanguageAnalyzer"""

class ApiError(GitLanguageAnalyzerError):
    """Raised when an API call fails"""

class RateLimitError(GitLanguageAnalyzerError):
    """Raised when API rate limit is exceeded"""

class UserNotFoundError(GitLanguageAnalyzerError):
    """Raised when a user is not found"""

class ConfigurationError(GitLanguageAnalyzerError):
    """Raised when there's an issue with the configuration"""