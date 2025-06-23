from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Resistances(Base):
    __tablename__ = 'resistances'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    value = Column(String)
