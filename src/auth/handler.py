from datetime import datetime, timedelta
from fastapi import Depends
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

from src.core.config import get_settings

ouath2_schema = OAuth2PasswordBearer(tokenUrl='Authorization')
config = get_settings()

class TokenHandler:
  @staticmethod
  def create_access_token(username: str):
    expiration = datetime.utcnow() + timedelta(seconds=config.jwt_expiration)
    data = {'sub': username, 'exp': expiration}
    encoded_jwt = jwt.encode(data, config.jwt_secret, algorithm=config.jwt_algorithm)

    return encoded_jwt

  @staticmethod
  def read_token(token: str):
    try:
      payload = jwt.decode(token, config.jwt_secret, algorithm=config.jwt_algorithm)
      username = payload.get('sub')

      if username is None:
        raise Exception('Invalid token')
      return username
    except JWTError:
      raise Exception('Invalid token')

def get_current_user(token: str = Depends(ouath2_schema)):
  return TokenHandler.read_token(token)