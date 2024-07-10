from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from inference import inference
app = FastAPI()

class TextRequest(BaseModel):
    text: str
@app.post("/generate-image/")
async def generate_image(request: TextRequest):
    try:
        image_path = inference(request.text)
        return {"image_path": image_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))