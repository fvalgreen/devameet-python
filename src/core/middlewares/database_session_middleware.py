from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from core.database import SessionLocal

class DatabaseSessionMiddleware(BaseHTTPMiddleware):
  def __init__(self, app):
    super().__init__(app)
  
  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
    response = Response("Internal Server Error", status_code=500)

    try:
      request.state.db = SessionLocal()
      response = await call_next(request)
    finally:
      request.state.db.close()

    return response
