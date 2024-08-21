from audio import get_user_input, say_answer
from openai_svc import answer_user_question
from vision import hasMadeEyeContact

def main():
    while True:
        contactMade = hasMadeEyeContact()
        if not contactMade:
            print('User elected to quit')
            break

        question = get_user_input()
        answer = answer_user_question(question)
        say_answer(answer)

if __name__ == '__main__':
    main()