from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class WishCards(Base):
    __tablename__ = 'wish_cards'

    # General Info
    id = Column(Integer, primary_key=True)
#    wish_id = Column(String, nullable=False, foreign_key=True)
    card_id = Column(String, nullable=False)

def __init__(self, id:int, card_id:str):
    self.id = id
    self.card_id = card_id