# Gemini Chat-Bot

Gemini Chat-Bot is a full-fledged conversational bot developed using Python, HTML, CSS, JavaScript, and Flask. It leverages the power of the Google AI model called "Gemini" through its API key to provide intelligent and engaging conversations. The bot is designed to be accessible through its website and is available as an open-source project on GitHub.

# Note
All the codes folders are inside src folder for the purpose of looking clean.

## Features

- **Conversational Intelligence:** Gemini Chat-Bot utilizes the latest Google AI model, "Gemini," to deliver advanced conversational abilities, making interactions more natural and engaging.

- **Web Interface:** Access the chat-bot conveniently through its user-friendly web interface. The web application is built using HTML, CSS, JavaScript, and Flask, ensuring a seamless user experience.

- **Open Source:** Gemini Chat-Bot is an open-source project, fostering collaboration and contributions from the community. Developers can explore, enhance, and customize the bot according to their requirements.

## Getting Started

### Prerequisites

Before running the Gemini Chat-Bot, ensure you have the following installed:

- Python
- Flask
- Gemini API key (available from the [Maker Suite Google](https://makersuite.google.com/))

### Installation

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/lokendarjangid/gemini-chat.git

2. Navigate to the project directory:

    ```bash
    cd gemini-chat
    ```

3. Set up the virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Install Google Cloud CLI:
    
    [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) is required to run the Gemini Chat-Bot.

6. Configure the Gemini API key:

    Copy the API key from the Make Suite Google and set it as an environment variable:

    replace the name of .env.example to .env and paste the API key in the .env file

7. Run the application:

    ```bash
    python app.py
    ```

Visit `http://127.0.0.1:5000` in your web browser to access the Gemini Chat-Bot.

## Contributing

We welcome contributions from the community. If you would like to contribute, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore and enhance the Gemini Chat-Bot project. If you encounter any issues or have suggestions for improvement, please create an issue on GitHub. Happy coding!
