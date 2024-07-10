import gradio as gr
from inference import generate_text_to_image

interface = gr.Interface(
    fn=generate_text_to_image,
    inputs=gr.Textbox(lines=2, placeholder="Enter your text prompt here..."),
    outputs="image",
    title="Demo Text to Image Generator",
    description="Enter a text prompt to generate an image based on the prompt."
)

# Launch the interface
interface.launch()