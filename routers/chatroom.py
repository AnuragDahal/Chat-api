from fastapi import APIRouter
from utils.chat_utils import ConnectionManager
from core.database import chat_collection
import uuid
from handlers.chathandler import (
    new_chat_room,
    check_room_id,
    get_conversation,
    
)
from models import schemas
from handlers.exception import ErrorHandler
manager = ConnectionManager()

router = APIRouter()




@router.get('/{room_id}')
async def get_conversation_by_room_id(room_id: str):

    # Get conversation by room id
    chats = get_conversation(room_id)
    return chats


@router.post('/initiate')
async def initiate():
    # Initiate a chat room
    room_id = new_chat_room()
    return room_id


@router.post('/{room_id}/message')
async def post_message(room_id: str, message: schemas.Message):
    '''Post a message to a chat room'''
    chats = check_room_id(room_id)
    if room_id in chats:
        chats[room_id].messages.append(message)
        return {"detail": "Message posted successfully"}
    return ErrorHandler.NotFound(f"detail: No chat found for room id {room_id}")

