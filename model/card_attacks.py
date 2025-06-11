from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base


class CardAttacks(Base):
    __tablename__ = 'card_attacks'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, nullable=False)
    attack_id = Column(Integer, nullable=False)

    card_obj = relationship('Card')
    attack_obj = relationship('Attacks')

def __init__(self, id:int, card_id:str, attack_id:int):
    self.id = id
    self.card_id = card_id
    self.attack_id = attack_id


