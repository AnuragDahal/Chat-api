from fastapi import APIRouter, WebSocketDisconnect, WebSocket
from utils.chat_utils import ConnectionManager
from core.database import chat_collection
from handlers.chathandler import (
    new_chat_room,
    check_room_id,
    get_conversation,

)
manager = ConnectionManager()

router = APIRouter(tags=['Chatroom'], prefix='/chatroom')

@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(websocket, room_id)
    await websocket.send_text(f"Connected to room {room_id}")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Message text was: {data} in room {room_id}", room_id)
    except WebSocketDisconnect:
        manager.disconnect(room_id)
        await manager.broadcast(f"Client #{room_id} left the chat")


# @router.get('/{room_id}')
# async def get_conversation_by_room_id(room_id: str):

#     # Get conversation by room id
#     chats = get_conversation(room_id)
#     return chats


# @router.post('/initiate')
# async def initiate():
#     # Initiate a chat room
#     room_id = new_chat_room()
#     return room_id


# @router.post('/{room_id}/message')
# async def post_message(room_id: str, message: schemas.Message):
#     '''Post a message to a chat room'''
#     chats = check_room_id(room_id)
#     if room_id in chats:
#         chats[room_id].messages.append(message)
#         return {"detail": "Message posted successfully"}
#     return ErrorHandler.NotFound(f"detail: No chat found for room id {room_id}")
