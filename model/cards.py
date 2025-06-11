from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base


class Cards(Base):
    __tablename__ = 'cards'

    # General Info
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    hp = Column(Integer, nullable=False)
    number = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    supertype = Column(Integer, nullable=False)
    rules = Column(String)

    # Images
    image_sm = Column(String)
    image_lg = Column(String)

    # Legalities
    unlimited = Column(Integer)
    expanded = Column(Integer)
    standard = Column(Integer)

    attack_obj = relationship('CardAttacks')
    supertype_obj = relationship('Supertype')
    subtype_obj = relationship('CardSubtypes')
    type_obj = relationship('CardTypes')
    resistance_obj = relationship('CardResistance')
    weakness_obj = relationship('CardWeaknesses')
    ability_obj = relationship('CardAbilities')

def __init__(self, id:str, name:str, hp:int, number:int, rarity:int, supertype:int, image_sm:str, image_lg:str,
             unlimited:int, expanded:int, standard:int):
    self.id = id
    self.name = name
    self.hp = hp
    self.number = number
    self.rarity = rarity
    self.supertype = supertype
    self.image_sm = image_sm
    self.image_lg = image_lg
    self.unlimited = unlimited
    self.expanded = expanded
    self.standard = standard
