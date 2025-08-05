from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine, AzureEngine, ElevenlabsEngine
import cohere
import pyttsx3

def speak_english(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()


# Initialize Cohere (replace with your API key)
co = cohere.Client("Key")  # <<<--- INSERT YOUR API KEY

def generate_response(text):
    response = co.chat(
        message=text,
        model="command",
        temperature=0.3,
        preamble="You are a helpful assistant, alway answer with less than 15 words"
    )
    return response.text.strip()

def main():
    # Initialize components
    recorder = AudioToTextRecorder()
    engine = SystemEngine()
    tts = TextToAudioStream(engine)

    while True:
        print("Speak now (press Enter to stop)...")
        recorder.start()
        input()  # Wait for Enter key
        recorder.stop()

        user_input = recorder.text().strip()
        print(f"\nYou said: {user_input}")

        if not user_input:
            print("Didn't catch that. Try again.\n")
            continue

        if user_input.lower() in ["exit.", "quit.", "bye."]:
            print("Goodbye!")
            break

        if user_input.strip():
            
            ai_response = generate_response(user_input)
            print("AI Response:", ai_response)

            
            speak_english(ai_response)


if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
