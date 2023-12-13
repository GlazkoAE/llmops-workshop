from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

# import deepseek
import vllm_inference

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateCodeRequest(BaseModel):
    prompt: str


@app.post("/")
async def generate_code(request: GenerateCodeRequest):
    generated_code = vllm_inference.generate(prompt=request.prompt)
    return {"code": generated_code}
