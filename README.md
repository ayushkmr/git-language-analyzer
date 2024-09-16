# Git Language Analyzer

Git Language Analyzer is a sophisticated Python-based command-line tool designed to analyze and visualize the programming languages used across a user's Git repositories. It currently offers robust support for two major Git platforms: GitHub and GitLab.

## Features

- Comprehensive analysis of programming languages used in a user's repositories
- Calculation and display of the top 5 most frequently used languages
- Percentage breakdown of language usage across all repositories
- Multi-provider support with extensible architecture (currently GitHub and GitLab)
- Flexible and customizable API settings for each supported Git provider
- Robust error handling for common issues (e.g., rate limiting, authentication errors)
- Detailed logging system for in-depth debugging and performance monitoring

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ayushkmr/git-language-analyzer.git
   cd git-language-analyzer
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before using the Git Language Analyzer, you must configure the API settings for each Git provider you intend to use. This process involves the following steps:

1. Run the application: `python src/main.py`
2. Choose option 1 to configure a Git provider
3. Provide the following information:
   - Provider name (choose either 'github' or 'gitlab')
   - API URL:
     - For GitHub: https://api.github.com
     - For GitLab: https://gitlab.com/api/v4
   - Your personal access token for the chosen provider
     - For GitHub: Generate a token at https://github.com/settings/tokens
     - For GitLab: Generate a token at https://gitlab.com/-/profile/personal_access_tokens

Note: Ensure your access token has the necessary permissions to read repository data.

## Usage

To start the application, run:
```
python src/main.py
```

Once the application is running, you'll be presented with a menu:

1. Configure Git Provider
2. Analyze Profile
3. Exit

Choose the appropriate option by entering the corresponding number.

### Analyzing a Profile

1. Select option 2 from the main menu.
2. Enter the Git profile URL you want to analyze (e.g., https://github.com/ayushkmr).
3. The application will fetch and analyze the repositories, then display the top 5 most used programming languages along with their usage percentages.

## Running Tests

To run the test suite, follow these steps:

1. Ensure you're in the project root directory and your virtual environment is activated.

2. Install pytest if you haven't already:
   ```
   pip install pytest
   ```

3. Run the tests:
   ```
   pytest
   ```

This will discover and run all test files in the project.

For more detailed test output, you can use the following command:
```
pytest -v
```

## Troubleshooting

If you encounter any issues:

1. Check the `git_language_analyzer.log` file for detailed error messages and debugging information.
2. Ensure your Git provider access token has the necessary permissions.
3. Verify your internet connection if you're having trouble connecting to the Git provider's API.
4. Make sure you've correctly configured the Git provider in the application settings.

If problems persist, please open an issue on the GitHub repository with a detailed description of the error and the steps to reproduce it.