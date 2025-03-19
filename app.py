from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import uvicorn
import os

from src import generate_response

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    message: str
    model: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: ChatRequest):
    if request.model == "openai":
        answer = generate_response(request.message)
    elif request.model == "llama":
        answer = "Use ai8.breezemytrip.com for Llama"
    elif request.model == "falcon":
        answer = "Use ai8.breezemytrip.com for Falcon"
    else:
        answer = "Invalid model selection"
    return {"response": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8007)
