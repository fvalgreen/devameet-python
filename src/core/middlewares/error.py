import traceback
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import HTTPException, Request, Response
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import sqlalchemy.exc

from src.core.logger import ApiLogger

class ApiError(Exception):
  def __init__(self, message, error, status_code=500):
    self.message = message
    self.error = error
    self.status_code = status_code
  
  def __str__(self):
    return self.message

class ErrorConverterMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
    try:
      return await call_next(request)
    except Exception as e:
      logger = ApiLogger(name='ErrorConverterMiddleware')
      traceback.print_exc()

      if isinstance(e, ApiError):
        raise
      error_dict = {
        404: 'Item not Found',
        500: 'Internal Server Error'
      }

      message = str(e)
      status_code = 500

      logger.debug(f'Error type: {e}')

      if isinstance(e, sqlalchemy.exc.NoResultFound):
        status_code = 404

      raise ApiError(message=message, error=error_dict[status_code], status_code=status_code)
    

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
    try:
      return await call_next(request)
    except ApiError as e:
      return JSONResponse(
        status_code=e.status_code,
        content={
          'message': e.message.split(';'),
          'error': e.error,
          'statusCode': e.status_code
        }
      )

def handle_http_exception(request: Request, exc: HTTPException):
  raise ApiError(message=exc.detail, error=exc.detail, status_code=exc.status_code)

def handle_validation_error(request: Request, exc: RequestValidationError):
  errors = ';'.join(get_error_message(err) for err in exc.errors())


  raise ApiError(message=errors, error='UnprocessableEntity', status_code=422)

def get_error_message(error):
  logger = ApiLogger(name='hand;e_validation_error')
  logger.debug(f'Error dictionary: {error}')

  if error['type'] == 'value_error.missing':
    return f"Missing value for {error['loc']}"
  else:
    header = error['loc'][-1].capitalize()
    return f'{header}: {error["msg"]}'