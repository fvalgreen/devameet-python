from fastapi import APIRouter, Body, Depends

from src.auth.handler import get_current_user
from .schema import UpdateUser
from .service import UserServices


router = APIRouter()

@router.get('/')
async def read_users_me(username: str = Depends(get_current_user),service: UserServices = Depends(UserServices)):
  return service.get_user_by_username(username)

@router.put('/{id}')
async def register(
  id: str,
  dto: UpdateUser = Body(embed=False),
  username: str = Depends(get_current_user), 
  service: UserServices = Depends(UserServices)):  
  return service.update_user(id, username, dto)
