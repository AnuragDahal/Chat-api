from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, room_id: str):
        await websocket.accept()
        self.active_connections[room_id] = websocket

    async def disconnect(self, room_id: str):
        await self.active_connections[room_id].close()
        del self.active_connections[room_id]

    async def send_message(self, message: str, room_id: str):
        await self.active_connections[room_id].send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)


app = FastAPI()


@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Message text was: {data} in room {room_id}", room_id)
    except WebSocketDisconnect:
        manager.disconnect(room_id)
        await manager.broadcast(f"Client #{room_id} left the chat")
