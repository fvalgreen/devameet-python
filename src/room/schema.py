from pydantic import BaseModel, Field


class UpdatePosition(BaseModel):
  direction: str = Field(..., regex='(up|right|left|down)')

class CreateUserPosition(BaseModel):
  x: int = Field(..., ge=0, le=7)
  y: int = Field(..., ge=0, le=7)
  orientation: str = Field(..., regex='(back|right|left|front)')
  
class ToggleMute(BaseModel):
  user_id: str
  link: str
  muted: bool
  user_to_mute: str