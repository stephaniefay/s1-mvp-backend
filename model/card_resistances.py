from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base
from model.cards import Cards
from model.resistances import Resistances

class CardResistances(Base):
    __tablename__ = 'card_resistances'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, ForeignKey(Cards.id), nullable=False)
    resistance_id = Column(Integer, ForeignKey(Resistances.id), nullable=False)

    card_obj = relationship('Cards')
    resistance_obj = relationship('Resistances')

def __init__(self, id:int, card_id:str, resistance_id:int):
    self.id = id
    self.card_id = card_id
    self.resistance_id = resistance_id
