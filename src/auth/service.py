from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from .handler import TokenHandler

from src.core.database import get_db
from .model import User
from .schema import Login, Register, Token


class AuthServices:

  def __init__(self, db: Session = Depends(get_db)):
    self.db = db
    self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

  def login(self, dto: Login):
    user = self.db.query(User).filter(User.username == dto.login).first()

    if not user:
      raise Exception('Incorrect username or password')
    if not self.pwd_context.verify(dto.password, user.hashed_password):
      raise Exception('Incorrect username or password')
    
    token = TokenHandler.create_access_token(user.username)
    return Token(email=user.username, name=user.name, token=token)


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



