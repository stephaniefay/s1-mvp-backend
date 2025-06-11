from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


from model import Base


class Series(Base):
    __tablename__ = 'series'

    # General Info
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

def __init__(self, id:int, name:str):
    self.id = id
    self.name = name

