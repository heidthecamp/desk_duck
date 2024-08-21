from gradio_client import Client, handle_file

client = Client("abidlabs/whisper")

client.predict(
    audio=handle_file("audio_sample.wav")
)

