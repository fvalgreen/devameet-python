from fastapi import APIRouter

from .config import get_settings
from .logger import ApiLogger

router = APIRouter()

@router.get('/')
async def root():
  settings = get_settings()
  api_logger = ApiLogger()

  api_logger.debug('This is a debug line')
  api_logger.info('This is a info line')
  api_logger.warning('This is a warn line')
  api_logger.error('This is a error line')
  api_logger.critical('This is a critical line')

  return {'message': 'Hello world', 'log_level': settings.log_level}

@router.get('/teste')
async def root():
  return {'message': 'Teste 2'}