from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    email: str
    password: str

class UpdateUserEmail(BaseModel):
    email: str


class Message(BaseModel):
    user_id: str
    content: str

class Chat(BaseModel):
    room_id: str
    messages: List[Message] = []
