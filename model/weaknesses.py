from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Weaknesses(Base):
    __tablename__ = 'weaknesses'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    value = Column(String)
