from fastapi import APIRouter, Body, Depends

from src.auth.handler import get_current_user
from .schema import CreateMeet, UpdateMeet
from .service import MeetServices


router = APIRouter()

@router.post('/')
async def create_meet(
  dto: CreateMeet = Body(...),
  username: str = Depends(get_current_user),
  service: MeetServices = Depends(MeetServices)):

  return service.create_meet(dto)

@router.get('/')
async def get_all(
  username: str = Depends(get_current_user),
  service: MeetServices = Depends(MeetServices)):

  return service.get_all()

@router.get('/{id}')
async def get_all(
  id: str,
  username: str = Depends(get_current_user),
  service: MeetServices = Depends(MeetServices)):

  return service.get_by_id(id)

@router.put('/{id}')
async def update_meet(
  id: str,
  dto: UpdateMeet = Body(embed=False),
  username: str = Depends(get_current_user), 
  service: MeetServices = Depends(MeetServices)):  
  return service.update_meet(id, dto)

@router.delete('/{id}')
async def delete_meet(id: str, username: str = Depends(get_current_user), service: MeetServices =  Depends(MeetServices)):
  return service.delete_meet(id)

