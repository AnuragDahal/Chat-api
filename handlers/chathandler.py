from core.database import chat_collection
from .exception import ErrorHandler
import uuid


def check_room_id(room_id: str):

    # ? Check if a chat room exists

    chats = chat_collection.find_one({"room_id": room_id})
    if room_id in chats:
        return room_id
    return ErrorHandler.NotFound(f"{room_id} not found")


def get_conversation(room_id: str):
    # verify room_id
    verified_room_id = check_room_id(room_id)
    # if room id is found, return the chat
    chats = chat_collection.find_one({"room_id": verified_room_id})

    return chats[verified_room_id]


def new_chat_room():
    # Initiate a chat room
    room_id = str(uuid.uuid4())
    chat_collection.insert_one({"room_id": room_id, "messages": []})
    return {"room_id": room_id}


def store_message(room_id: str, message: str):
    # Store message in the database
    chat_collection.update_one({"room_id": room_id}, {
                               "$push": {"messages": message}})