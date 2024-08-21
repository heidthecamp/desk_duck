import speech_recognition as sr
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
    engine = gTTS(text=answer, lang='en', slow=False)

    #save the speech to a file
    engine.save("answer.mp3")

    
    # Play the saved audio file
    # Platform-specific command to play audio
    if os.name == 'nt':  # Windows
        os.system("start answer.mp3")
    elif os.name == 'posix':  # macOS or Linux
        if 'darwin' in os.uname().sysname.lower():  # macOS
            os.system("afplay answer.mp3")
        else:  # Linux
            os.system("mpg321 answer.mp3")  # or use `mplayer` instead

# Example usage:
if __name__ == "__main__":
    while True:
        user_question = get_user_input()
        if user_question.lower() in ['exit', 'quit', 'stop']:
            print("Conversation ended.")
            break
        
        say_answer(user_question)
