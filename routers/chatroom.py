from fastapi import APIRouter , WebSocket
from utils.chat_utils import ConnectionManager
from core.database import chat_collection


manager=ConnectionManager()

router = APIRouter()


# In-memory storage for chats

@router.get('/{room_id}')
async def get_conversation_by_room_id(room_id: str):

    chats=chat_collection.find_one({"room_id":room_id})
    
    
    # Return the chat by room id
    # if room_id in chats:
    #     return chats[room_id]
    # return {"detail": f"No chat found for room id {room_id}"}

@router.post('/initiate')
async def initiate():
    # Initiate a new chat
    # Create a new chat room and return the room id
        room_id=

@router.post('/{room_id}/message')
async def post_message(room_id: str, message: Message):
    # Post a message in a chat room
    if room_id in chats:
        chats[room_id].messages.append(message)
        return {"detail": "Message posted successfully"}
    return {"detail": f"No chat found for room id {room_id}"}

@router.put('/{room_id}/mark-read')
async def mark_conversation_read_by_room_id(room_id: str):
    # Mark conversation as read by room id
    # This is a placeholder operation as we don't have a 'read' status in this simplified example
    if room_id in chats:
        return {"detail": f"Chat {room_id} marked as read"}
    return {"detail": f"No chat found for room id {room_id}"}