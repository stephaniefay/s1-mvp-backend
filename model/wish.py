from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base

class Wish(Base):
    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)

def __init__(self, name:str, description:str):
    self.name = name
    self.description = description