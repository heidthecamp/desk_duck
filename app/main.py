from audio import get_user_input, say_answer
from openai_svc import answer_user_question
from vision import hasMadeEyeContact
from gradio_client import Client, handle_file

def transcribe_audio():
    client = Client("abidlabs/whisper")
    result = client.predict(
        audio=handle_file("audio_sample.wav")
    )
    return result

def main():
    while True:
        contactMade = hasMadeEyeContact()
        if not contactMade:
            print('User elected to quit')
            break
        # You can integrate the transcribed audio result here
        transcription = transcribe_audio()
        print(f"Transcription: {transcription}")  # Print the transcription or handle it as needed

        question = get_user_input()
        answer = answer_user_question(question)
        say_answer(answer)




import gradio as gr
from audio import get_user_input, say_answer
from openai_svc import answer_user_question
from vision import hasMadeEyeContact
from gradio_client import Client, handle_file

def transcribe_audio():
    client = Client("abidlabs/whisper")
    result = client.predict(
        audio=handle_file("audio_sample.wav")
    )
    return result

def activate_contact():
    main()


def app():
    with gr.Blocks() as demo:
        btn = gr.Button("Show me something cool")
        output_text = gr.Textbox(label="Status")

        btn.click(fn=activate_contact, outputs=output_text)

    demo.launch()

if __name__ == '__main__':
    app()
