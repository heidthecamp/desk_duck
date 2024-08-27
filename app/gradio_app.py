import gradio as gr
from main import main

def activate_contact(_):
    main()


def app():
    gr.Interface(fn=activate_contact, inputs=[gr.Button()], outputs=None).launch(share=True)
    

if __name__ == '__main__':
    app()