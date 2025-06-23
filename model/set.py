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
