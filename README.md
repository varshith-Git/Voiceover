# Voiceover

This project creates a custom voice by analyzing a training audio file and synthesizing speech in the same voice.

## Features

- Capture and transcribe voice input
- Convert text to speech
- Supports custom voices
- Web-based GUI using Flask

## Requirements

- Python 3.8+
- Flask
- SpeechRecognition
- Pyttsx3
- python-dotenv

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/varshith-Git/Voiceover.git
    cd Voiceover
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file for environment variables (if needed):
    ```bash
    touch .env
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Upload an audio file or use the microphone to capture voice input.


