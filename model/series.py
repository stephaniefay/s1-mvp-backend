from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


from model import Base


class Series(Base):
    __tablename__ = 'series'

    # General Info
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    acronym = Column(String, nullable=True)

def __init__(self, id:int, name:str, acronym:str):
    self.id = id
    self.name = name
    self.acronym = acronym

