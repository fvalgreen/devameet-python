

import random
import string
from sqlalchemy import Column, Integer, String
from src.core.database import Base


class Meet(Base):
  __tablename__ = 'meets'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), index=True, nullable=False)
  color = Column(String(7), nullable=False, default='#000000')
  link = Column(String(100), index=True, nullable=False)

  def __init__(self, **kwargs):
    super(Meet, self).__init__(**kwargs)

    if not self.link:
      self.link = MeetLinkGenerator.generate()

class MeetLinkGenerator:
  @staticmethod
  def generate_link_section(length):
    characters = string.ascii_lowercase + string.digits

    return ''.join(random.choice(characters) for _ in range(length))

  @staticmethod
  def generate():
    return '-'.join([MeetLinkGenerator.generate_link_section(3),
                     MeetLinkGenerator.generate_link_section(4),
                     MeetLinkGenerator.generate_link_section(3)])
  


