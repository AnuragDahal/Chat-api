import asyncio
import websockets
from handlers.chathandler import new_chat_room


async def connect_to_websocket():
    # Create a new room and get its ID
    room_id = await new_chat_room()

    uri = f"ws://localhost:8000/chatroom/ws/{room_id["room_id"]}"
    async with websockets.connect(uri) as websocket:
        # Send a message
        await websocket.send("Hello, world!")
        # Receive a message
        response = await websocket.recv()
        print(response)

# Run the function*
asyncio.run(connect_to_websocket())
