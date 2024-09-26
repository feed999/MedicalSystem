from sqlalchemy import Column, Integer, String

from app.database import Base


class Status(Base):
    __tablename__ = "statuses"
    
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False) 
    