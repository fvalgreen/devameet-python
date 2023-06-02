from fastapi import FastAPI
from src.core.config import get_settings

app = FastAPI()

@app.get('/')
async def root():
  settings = get_settings()
  return {'message': 'Hello world', 'log_level': settings.log_level}

@app.get('/teste')
async def root():
  return {'message': 'Teste 2'}