from fastapi import FastAPI
from pydantic import BaseModel
from backend.chain import run_chain

app = FastAPI(title="AI Memory Brain")

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    reply = run_chain(req.user_id, req.message)
    return {"response": reply}