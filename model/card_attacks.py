from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base
from model.cards import Cards
from model.attacks import Attacks


class CardAttacks(Base):
    __tablename__ = 'card_attacks'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, ForeignKey(Cards.id), nullable=False)
    attack_id = Column(Integer, ForeignKey(Attacks.id), nullable=False)

    card_obj = relationship('Cards')
    attack_obj = relationship('Attacks')
