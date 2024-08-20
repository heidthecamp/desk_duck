
# def get_user_input() -> str:
#     return input("Please enter your question: ")

# def say_answer(answer: str):
#     print(answer)

import speech_recognition as sr
# import pyttsx3

from pathlib import Path
from openai import OpenAI

import sounddevice as sd
import soundfile as sf
import io


import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def get_user_input() -> str:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    attempt = 0

    while attempt < 3:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for your question...")
            audio = recognizer.listen(source)
        try:
            print("Recognizing speech...")
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
            attempt += 1
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
            return ""
    return ""

def say_answer(answer: str):
    print(answer)
    spoken_response = client.audio.speech.create(
    model="tts-1-hd",
    voice="shimmer",
    response_format="opus",
    input=answer
    )

    buffer = io.BytesIO()
    for chunk in spoken_response.iter_bytes(chunk_size=4096):
        buffer.write(chunk)
    buffer.seek(0)

    with sf.SoundFile(buffer, 'r') as sound_file:
        data = sound_file.read(dtype='int16')
        sd.play(data, sound_file.samplerate)
        sd.wait()

if __name__ == "__main__":
    while True:
        user_question = get_user_input()
        if user_question.lower() in ['exit', 'quit', 'stop']:
            say_answer("Conversation ended.")
            break

        say_answer(user_question)
