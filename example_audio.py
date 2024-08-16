# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
import speech_recognition as sr
import pyttsx3 as tts

r = sr.Recognizer()

def SpeakText(command):
    engine = tts.init()
    engine.say(command)
    engine.runAndWait()

while(True):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say: "+MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")