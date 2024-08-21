import gradio as gr
from main import main

def activate_contact():
    main()


def app():
    # with gr.Blocks() as demo:
    #     btn = gr.Button("Show me something cool")
    #     output_text = gr.Textbox(label="Status")

    #     btn.click(fn=activate_contact, outputs=output_text)

    # demo.launch()

    gr.Interface(fn=activate_contact, inputs=None, outputs=None).launch()
    

if __name__ == '__main__':
    app()