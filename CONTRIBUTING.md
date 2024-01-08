# Contributing to Gemini Chat

Welcome to Gemini Chat's community! We appreciate contributions. Follow these guidelines to contribute.

## Getting Started

### Prerequisites

- Python (version 3.9 or later)
- Flask (version 3.0.x or later)
- (google cloud CLI)[https://cloud.google.com/sdk/docs/install]
- Other required libraries (install using pip install -r requirements.txt)
- Gemini API key (obtain from the [Maker Suite Google](https://makersuite.google.com/app/apikey))
- Google Cloud CLI
### Installation

#### 1.Clone the repository:
```Bash
git clone https://github.com/lokendarjangid/gemini-chat.git
```
```Bash
cd gemini-chat-bot
```

#### 2.Create a virtual environment (optional but recommended):
```Bash
python -m venv venv
source venv/bin/activate
```
 On Windows, use `venv\Scripts\activate`

#### 3.Install dependencies:
```Bash
pip install -r requirements.txt
```
### Configuring the Gemini API Key

1. Copy your Gemini API key from the [Maker Suite Google](https://makersuite.google.com/app/apikey).
2. Create a `.env` file in the project directory (if not already present).
3. Paste the API key into the `.env` file as follows:
    ```
    GEMINI_API_KEY="your_api_key_here'
    ```

## Contributing Guidelines

### Suggesting Features or Reporting Bugs

- Use the GitHub issue tracker for feature requests or bug reports.
- Provide clear and detailed descriptions, including:
    - Steps to reproduce the issue (if applicable)
    - Expected behavior
    - Actual behavior

### Making Changes

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Make changes and commit them with clear messages.
4. Push changes to your fork.
5. Open a pull request from your fork to the main repository.

### Testing

- Run the existing test suite to ensure changes don't introduce new bugs.
- Add new tests if necessary.

### Documentation

- Update existing documentation to reflect changes.
- Add new documentation for new features.

## Community

- Use the GitHub issue tracker for discussions and questions.
- Participate in code reviews to improve code quality.

## Additional Information

- **Contribution Review Process:** We'll review pull requests and provide feedback promptly.
- **Good First Issues:** Issues labeled as "good first issue" in the tracker are suitable for new contributors.
- **Relevant Resources:**
    - [Google Cloud documentation](https://cloud.google.com/docs)
    - Contributing guides for popular libraries (e.g., Flask, Python): [Flask](https://flask.palletsprojects.com/en/2.2.x/contributing/), [Python](https://devguide.python.org/)

Thank you for your interest in contributing to Gemini Chat!
