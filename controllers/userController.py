from fastapi import HTTPException, status,APIRouter, HTTPException
from services.userServices import retrieve_users, add_user, retrieve_user, update_user, delete_user
from models.userModel import userCreate, userUpdate, userSchema, userDelete
from typing import List

router = APIRouter()

@router.post("/users/", response_model=userSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: userCreate):
    user_dict = user.dict(exclude_unset=True, exclude={"id"})
    new_user = await add_user(user_dict)
    return new_user


@router.get("/users/", response_model=List[userSchema])
async def get_users():
    return await retrieve_users()

@router.get("/users/{id}", response_model=userSchema)
async def get_user(id: str):
    user = await retrieve_user(id)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

@router.put("/users/{id}", response_model=userSchema)
async def update_user_data(id: str, user: userUpdate):
    if await update_user(id, user.dict()):
        return await retrieve_user(id)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Update failed or user not found")

@router.delete("/users/{id}", response_model=userDelete)
async def delete_user_data(id: str):
    if await delete_user(id):
        return {"message": "user deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

