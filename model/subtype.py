from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from model import Base


class Subtype(Base):
    __tablename__ = 'subtype'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
