from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base
from model.cards import Cards
from model.type import Type

class CardTypes(Base):
    __tablename__ = 'card_types'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, ForeignKey(Cards.id), nullable=False)
    type_id = Column(Integer, ForeignKey(Type.id), nullable=False)

    card_obj = relationship('Cards')
    type_obj = relationship('Type')

def __init__(self, id:int, card_id:str, type_id:int):
    self.id = id
    self.card_id = card_id
    self.type_id = type_id
