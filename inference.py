from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch
from utils.database import upload_zip_file_to_s3

def generate_text_to_image(text):
    model_id = "stabilityai/stable-diffusion-2-1"
    image_path_saved = "images/sd2_1_base.png"

    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    print(f"pipe {pipe.device}")

    # prompt = "a photo of an astronaut riding a horse on earth"
    prompt = text
    image = pipe(prompt).images[0]  
    image.save(image_path_saved)
    return image_path_saved

def inference(text):
    model_id = "stabilityai/stable-diffusion-2-1-base"
    image_path_saved = "images/sd2_1_base.png"

    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    print(f"pipe {pipe.device}")

    # prompt = "a photo of an astronaut riding a horse on earth"
    prompt = text
    image = pipe(prompt).images[0]  
    image.save("images/sd2_1_base.png")
    filename = image_path_saved.split("/")[-1]
    file_url, err = upload_zip_file_to_s3(image_path_saved,
                                          f"{filename}")
    if err:
        return f"Error: {str(err)}"
    return file_url