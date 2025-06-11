from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base
from model.set import Set
from model.cards import Cards

class SetCards(Base):
    __tablename__ = 'set_cards'

    # General Info
    id = Column(Integer, primary_key=True)
    set_id = Column(String, ForeignKey(Set.id), nullable=False)
    card_id = Column(String, ForeignKey(Cards.id), nullable=False)

    set_obj = relationship('Set')
    card_obj = relationship('Cards')

def __init__(self, id:int, set_id:str, card_id:str):
    self.id = id
    self.set_id = set_id
    self.card_id = card_id
