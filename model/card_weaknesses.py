from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base
from model.cards import Cards
from model.weaknesses import Weaknesses

class CardWeaknesses(Base):
    __tablename__ = 'card_weaknesses'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(Integer, ForeignKey(Cards.id), nullable=False)
    weakness_id = Column(Integer, ForeignKey(Weaknesses.id), nullable=False)

    card_obj = relationship('Cards')
    weakness_obj = relationship('Weaknesses')

def __init__(self, id:int, card_id:int, weakness_id:int):
    self.id = id
    self.card_id = card_id
    self.weakness_id = weakness_id
