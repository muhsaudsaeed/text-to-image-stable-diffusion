# Text to Image Generation with Stable Diffusion

This repository provides code to generate images from text using the Stable Diffusion model. The generated images can be saved locally and uploaded to AWS S3 for easy access.

## Features
- Generate images from text prompts using Stable Diffusion.
- Save generated images locally.
- Upload generated images to S3.
- FastAPI endpoint for generating images from prompts.
- Gradio interface for generating images interactively.

## Requirements

- Python 3.10.12
- torch
- diffusers
- boto3
- FastAPI
- Python-dotenv
- Gradio
- CUDA-enabled GPU or Apple Silicon GPU (MPS)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/text-to-image-stable-diffusion.git
    cd text-to-image-stable-diffusion
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have AWS credentials configured for S3 upload in a `.env` file:
    ```
    AWS_ACCESS_KEY_ID=your_access_key_id
    AWS_SECRET_ACCESS_KEY=your_secret_access_key
    AWS_S3_BUCKET_NAME=your_bucket_name
    ```

## Usage

To generate an image from a text prompt, use the `generate_text_to_image` or `inference` function from the `main.py` script. You can also use the FastAPI endpoint for generating images or the Gradio interface for interactive generation.

### Example

1. Import the required functions:
    ```python
    from main import generate_text_to_image, inference
    ```

2. Generate an image from a text prompt:
    ```python
    text_prompt = "a photo of an astronaut riding a horse on earth"
    image_path = generate_text_to_image(text_prompt)
    print(f"Image saved at: {image_path}")
    ```

3. Alternatively, generate an image and upload it to S3:
    ```python
    text_prompt = "a photo of an astronaut riding a horse on earth"
    image_url = inference(text_prompt)
    print(f"Image URL: {image_url}")
    ```

4. To use the FastAPI endpoint, run the API server:
    ```sh
    uvicorn main:app --reload
    ```

5. Make a POST request to the endpoint with your prompt:
    ```sh
    curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"prompt": "a photo of an astronaut riding a horse on earth"}'
    ```

6. To use the Gradio interface, run the script:
    ```sh
    python test_gradio.py
    ```

## Directory Structure
text-to-image-stable-diffusion/
├── images/                      # Directory to save generated images
├── utils/
│   └── database.py              # Contains the S3 upload function
├── main.py                      # Main script with generation functions and FastAPI endpoint
├── test_gradio.py               # Script for Gradio interface
├── requirements.txt             # Python dependencies
└── README.md                    # This file

## Configuration

To switch between different versions of the Stable Diffusion model, change the `model_id` in the `main.py` file:
- For the standard model: `"stabilityai/stable-diffusion-2-1"`
- For the base model: `"stabilityai/stable-diffusion-2-1-base"`

### GPU Configuration

- For NVIDIA GPUs:
    ```python
    pipe = pipe.to("cuda")
    ```

- For Apple Silicon (M1/M2) GPUs:
    ```python
    pipe = pipe.to("mps")
    ```
