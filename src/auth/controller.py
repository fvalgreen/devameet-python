from fastapi import APIRouter, Depends

from .service import AuthServices
from .schema import Login, Register

router = APIRouter()

@router.post('/login')
async def login(dto: Login, service: AuthServices = Depends(AuthServices)):
  return service.login(dto)

@router.post('/register')
async def register(dto: Register, service: AuthServices = Depends(AuthServices)):  
  return service.register(dto)
