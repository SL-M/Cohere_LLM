# Speech to AI Interaction

This project records audio, transcribes it, uses a Cohere LLM to generate a response, and plays back the reply as audio.

## Features:
- Speech-to-text via `RealtimeSTT`
- LLM response via `Cohere`
- Text-to-speech using `pyttsx3`
- Looping conversation with exit option

## How to Run
1. Install dependencies:
    ```
    pip install cohere pyttsx3
    ```

2. Replace `"Key"` with your Cohere API key.

3. Run the app:
    ```
    python main.py
    ```

## Exit Commands
Say: `exit.`, `quit.`, or `bye.`
