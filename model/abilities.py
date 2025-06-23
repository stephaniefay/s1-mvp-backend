from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Abilities(Base):
    __tablename__ = 'abilities'

    # General Info
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    text = Column(String)
    type = Column(String)
