from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Cost(Base):
    __tablename__ = 'cost'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    order = Column(Integer, nullable=False)
    id_ref = Column(String, nullable=False)
    type_ref = Column(String, nullable=False)

def __init__(self, id:int, type:int, order:int, id_ref:str, type_ref:str):
    self.id = id
    self.type = type
    self.order = order
    self.id_ref = id_ref
    self.type_ref = type_ref