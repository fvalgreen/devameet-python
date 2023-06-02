from fastapi import APIRouter

from .service import AuthServices
from .schema import Login

router = APIRouter()

@router.post('/login')
async def login(dto: Login):
  service = AuthServices()
  return service.login(dto)