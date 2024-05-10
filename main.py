from fastapi import FastAPI
from routers import user, auth, chatroom
from fastapi.middleware.cors import CORSMiddleware
from core.database import client, db

app = FastAPI(title="Chat App",
              description="Chat App API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    client.admin.command("ping")
    print("Connected to MongoDB")
except Exception as e:
    print("Failed to connect to MongoDB")
    print(e)


def root():
    return {"message": "Hello World"}


# include routers from routers folder
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(chatroom.router)
