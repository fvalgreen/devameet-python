from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.core.database import get_db
from .model import User
from .schema import Login, Register


class AuthServices:

  def __init__(self, db: Session = Depends(get_db)):
    self.db = db
    self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

  def login(self, dto: Login):
    if not (dto.login == 'admin@admin.com' and dto.password == 'senha_segura'):
      raise HTTPException(400, 'Invalid login or password')
    return { 'message': 'login success'}
  
  def register(self, dto: Register):
    
    hashed_password = self.pwd_context.hash(dto.password)

    user = User(
      name=dto.name,
      avatar=dto.avatar,
      username=dto.email,
      hashed_password=hashed_password
    )

    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)

    return user



