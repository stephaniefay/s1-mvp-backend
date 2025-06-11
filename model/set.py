from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base
from model.series import Series


class Set(Base):
    __tablename__ = 'set'

    # General Info
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    series = Column(Integer, ForeignKey(Series.id), nullable=False)
    collection_total = Column(Integer, nullable=False)
    release_date = Column(String)
    ptcgo_code = Column(String)

    # Legalities
    unlimited = Column(Integer)
    expanded = Column(Integer)
    standard = Column(Integer)

    # Images
    image_logo = Column(String)
    image_symbol = Column(String)

    series_obj = relationship("Series")

def __init__(self, id: str, name:str, series:int, collection_total:int, release_date:datetime, ptcgo_code:str,
             unlimited:int, expanded:int, standard:int, image_logo:str, image_symbol:str):
    self.id = id
    self.name = name
    self.series = series
    self.collection_total = collection_total
    self.release_date = release_date
    self.ptcgo_code = ptcgo_code
    self.unlimited = unlimited
    self.expanded = expanded
    self.standard = standard
    self.image_logo = image_logo
    self.image_symbol = image_symbol




