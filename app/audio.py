
# def get_user_input() -> str:
#     return input("Please enter your question: ")

# def say_answer(answer: str):
#     print(answer)

import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os

def get_user_input() -> str:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

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
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service; {e}")
        return ""

def say_answer(answer: str):
    print(answer)
    # engine = pyttsx3.init()
    engine = gTTS(text=answer, lang='en', slow=False)
    # engine.say(answer)
    #save the speech to a file
    engine.save("answer.mp3")
    # engine.runAndWait()
    
    # Play the saved audio file
    # Platform-specific command to play audio
    if os.name == 'nt':  # Windows
        os.system("start answer.mp3")
    elif os.name == 'posix':  # macOS or Linux
        if 'darwin' in os.uname().sysname.lower():  # macOS
            os.system("afplay answer.mp3")
        else:  # Linux
            os.system("mpg321 answer.mp3")  # or use `mplayer` instead
# answer = "This is the response to your question."
# say_answer(answer)

# Example usage:
# question = get_user_input()
# if question:
#     say_answer("This is the response to your question.")

if __name__ == "__main__":
    while True:
        user_question = get_user_input()
        if user_question.lower() in ['exit', 'quit', 'stop']:
            print("Conversation ended.")
            break
        
        # answer = "This is the response to your question."
        say_answer(user_question)
