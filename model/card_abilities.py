from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base

from model.cards import Cards
from model.abilities import Abilities


class CardAbilities(Base):
    __tablename__ = 'card_abilities'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, ForeignKey(Cards.id), nullable=False)
    ability_id = Column(Integer, ForeignKey(Abilities.id), nullable=False)

    card_obj = relationship('Cards')
    ability_obj = relationship('Abilities')
