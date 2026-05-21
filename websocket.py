from fastapi import APIRouter, WebSocket
from app.orchestrator import handle_user_message

router = APIRouter()

@router.websocket("/ws/voice")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        response = await handle_user_message(
            session_id="demo-session",
            transcript=data
        )

        await websocket.send_json(response)
