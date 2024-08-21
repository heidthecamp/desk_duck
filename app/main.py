from audio import get_user_input, say_answer
from openai_svc import answer_user_question
from vision import hasMadeEyeContact

# def transcribe_audio():
#     client = Client("abidlabs/whisper")
#     result = client.predict(
#         audio=handle_file("audio_sample.wav")
#     )
#     return result

def main():
    while True:
        contactMade = hasMadeEyeContact()
        if not contactMade:
            print('User elected to quit')
            break
        # You can integrate the transcribed audio result here
        # transcription = transcribe_audio()
        # print(f"Transcription: {transcription}")  # Print the transcription or handle it as needed

        question = get_user_input()
        answer = answer_user_question(question)
        say_answer(answer)

if __name__ == '__main__':
    main()