from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Base


class Cost(Base):
    __tablename__ = 'cost'

    # General Info
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    id_ref = Column(String, nullable=False)
    type_ref = Column(String, nullable=False)
