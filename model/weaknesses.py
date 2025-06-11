from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Weaknesses(Base):
    __tablename__ = 'weaknesses'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    value = Column(String)

def __init__(self, id:int, type:str, value:str):
    self.id = id
    self.type = type
    self.value = value