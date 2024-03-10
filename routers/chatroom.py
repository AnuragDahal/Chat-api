from fastapi import APIRouter , WebSocket
from utils.chat_utils import ConnectionManager

manager=ConnectionManager()

router = APIRouter()


# In-memory storage for chats
chats: Dict[str, Chat] = {}

@router.get('/')
async def get_recent_conversation():
    # Return the most recent chat
    if chats:
        recent_chat_id = sorted(chats.keys())[-1]
        return chats[recent_chat_id]
    return {"detail": "No chats available"}

@router.get('/{room_id}')
async def get_conversation_by_room_id(room_id: str):
    # Return the chat by room id
    if room_id in chats:
        return chats[room_id]
    return {"detail": f"No chat found for room id {room_id}"}

@router.post('/initiate')
async def initiate():
    # Initiate a new chat
    room_id = str(len(chats) + 1)  # Generate a new room id
    chats[room_id] = Chat(room_id=room_id)
    return {"room_id": room_id}

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