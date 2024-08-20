
# def get_user_input() -> str:
#     return input("Please enter your question: ")

# def say_answer(answer: str):
#     print(answer)

import speech_recognition as sr
import pyttsx3

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
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()

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
        
        answer = "This is the response to your question."
        say_answer(answer)
        