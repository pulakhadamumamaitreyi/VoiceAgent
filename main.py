from fastapi import FastAPI
from app.websocket import router as ws_router

app = FastAPI(title="Voice AI Agent")

app.include_router(ws_router)

@app.get("/")
async def health():
    return {"status": "running"}
