from fastapi import APIRouter, Body, Depends

from src.auth.handler import get_current_user
from .schema import CreateMeet
from .service import MeetServices


router = APIRouter()

@router.post('/')
async def create_meet(
  dto: CreateMeet = Body(...),
  username: str = Depends(get_current_user),
  service: MeetServices = Depends(MeetServices)):

  return service.create_meet(dto)

