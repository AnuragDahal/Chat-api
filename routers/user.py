from fastapi import APIRouter, status
from handlers.userhandler import UserManager
from typing import List
from models import schemas
router = APIRouter(tags=["User"], prefix="/user")


@router.post("/newuser", status_code=status.HTTP_201_CREATED,)
async def create_user(req: schemas.User):

    user = UserManager.create(req)
    return user


@router.get("/read", response_model=List[schemas.User], status_code=status.HTTP_200_OK,)
async def read_user():

    user = UserManager.read()
    return user


@router.patch("/update/{old_email}", response_model=schemas.User, status_code=status.HTTP_200_OK,)
async def update_user(old_email: str, request: schemas.UpdateUserEmail):

    update_data = UserManager.update(old_email, request)
    return update_data


@router.delete("/delete/{email}", status_code=status.HTTP_200_OK,)
async def delete_user(email: str):

    user = UserManager.delete(email)
    return user
