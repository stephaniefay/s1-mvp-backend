from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base
from model.cards import Cards
from model.subtype import Subtype

class CardSubtypes(Base):
    __tablename__ = 'card_subtype'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, ForeignKey(Cards.id), nullable=False)
    subtype_id = Column(Integer, ForeignKey(Subtype.id), nullable=False)

    card_obj = relationship('Cards')
    subtype_obj = relationship('Subtype')

def __init__(self, id: int, card_id: str, subtype_id: int):
    self.id = id
    self.card_id = card_id
    self.subtype_id = subtype_id
