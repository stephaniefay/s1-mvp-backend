from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Supertype(Base):
    __tablename__ = 'supertype'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
