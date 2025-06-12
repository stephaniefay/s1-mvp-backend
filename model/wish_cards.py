from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from model import Base, Cards
from model.wish import Wish

class WishCards(Base):
    __tablename__ = 'wish_cards'
    __table_args__ = (UniqueConstraint('wish_id', 'card_id', name='_wish_card_uc'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    wish_id = Column(Integer, ForeignKey(Wish.id), nullable=False)
    card_id = Column(String, ForeignKey(Cards.id), nullable=False)

    wish_obj = relationship("Wish")
    card_obj = relationship("Cards")

def __init__(self, wish_id:int, card_id:str):
    self.wish_id = wish_id
    self.card_id = card_id