from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base


class CardAbilities(Base):
    __tablename__ = 'card_abilities'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, nullable=False)
    type_id = Column(Integer, nullable=False)

    card_obj = relationship('Card')
    type_obj = relationship('Type')

def __init__(self, id:int, card_id:str, type_id:int):
    self.id = id
    self.card_id = card_id
    self.type_id = type_id
