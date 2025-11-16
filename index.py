from fastapi import FastAPI, Response, status
from models import load_image_model, generate_image
from utils import img_to_bytes

# app = FastAPI()
# pipe = load_image_model()
# @app.get("/generate/image",
#          responses={status.HTTP_200_OK: {"content": {"image/png": {}}}},
#          response_class=Response)
# def serve_text_to_image_model_controller(prompt: str):
    
#     output = generate_image(pipe, prompt)
#     return Response(content=img_to_bytes(output), media_type="image/png")



 
import httpx
from fastapi import FastAPI, Response

app = FastAPI()

@app.get(
    "/generate/bentoml/image",
    responses={status.HTTP_200_OK: {"content": {"image/png": {}}}},
    response_class=Response,
)
def serve_bentoml_text_to_image_controller(prompt: str):
    with httpx.AsyncClient() as client:
        response = client.post(
            "http://localhost:5000/generate", json={"prompt": prompt}
        )
    return Response(content=response.content, media_type="image/png")

