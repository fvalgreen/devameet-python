from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
  return {'message': 'Hello world'}

@app.get('/teste')
async def root():
  return {'message': 'Teste 2'}