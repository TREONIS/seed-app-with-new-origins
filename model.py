from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class YourModel(Base):
    __tablename__  = 'yourmodel'
    id             = Column(Integer, primary_key=True)
