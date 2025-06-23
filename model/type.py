from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Type(Base):
    __tablename__ = 'type'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
