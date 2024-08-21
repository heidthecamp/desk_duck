from audio import get_user_input, say_answer
from openai_svc import answer_user_question
from vision import hasMadeEyeContact
import os
from sys import platform

if platform == 'win32':
    import winsound

def main():
    while True:
        contactMade = hasMadeEyeContact()
        if not contactMade:
            print('User elected to quit')
            break
        # ping the user to alert them that the conversation is starting
        # get user operating system and play the beep sound for given os
        if platform == "linux" or platform == "linux2":
            os.system("beep -f 555 -l 460")
        elif platform == "darwin":
            os.system("afplay /System/Library/Sounds/Ping.aiff")
        elif platform == "win32":
            winsound.Beep(555, 460)
        try:
            question = get_user_input()
            if question.lower() in ['exit', 'quit', 'stop']:
                say_answer("Conversation ended, Desk Duck out!")
                break
            
            elif question == "":
                say_answer("Sorry, I did not hear you.")
                continue
            answer = answer_user_question(question)
            say_answer(answer)
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == '__main__':
    main()