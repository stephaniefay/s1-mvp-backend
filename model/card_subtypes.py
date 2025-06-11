from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base


class CardSubtypes(Base):
    __tablename__ = 'card_subtype'

    # General Info
    id = Column(Integer, primary_key=True)
    card_id = Column(String, nullable=False)
    subtype_id = Column(Integer, nullable=False)

    card_obj = relationship('Card')
    subtype_obj = relationship('Subtypes')

def __init__(self, id: int, card_id: str, subtype_id: int):
    self.id = id
    self.card_id = card_id
    self.subtype_id = subtype_id
