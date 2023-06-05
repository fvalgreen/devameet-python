from fastapi import APIRouter, Body, Depends

from src.auth.handler import get_current_user
from .service import RoomServices


router = APIRouter()

@router.get('/{link}')
async def get_room(
  link: str,
  username: str = Depends(get_current_user),
  service: RoomServices = Depends(RoomServices)):

  return service.get_room(link)