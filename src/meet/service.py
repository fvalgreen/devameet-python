from fastapi import Depends

from src.core.middlewares.error import ApiError
from src.core.database import SessionLocal, get_db
from .model import Meet
from .schema import CreateMeet



class MeetServices:
  def __init__(self, db: SessionLocal = Depends(get_db)):
    
    self.db = db
  
  def create_meet(self, dto: CreateMeet):
    meet = Meet(name=dto.name, color=dto.color)

    self.db.add(meet)
    self.db.commit()
    self.db.refresh(meet)

    return meet