from fastapi import WebSocket
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