from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Attacks(Base):
    __tablename__ = 'attacks'

    # General Info
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    damage = Column(String)
    text = Column(String)

def __init__(self, id:int, name:str, damage:str, text:str):
    self.id = id
    self.name = name
    self.damage = damage
    self.text = text