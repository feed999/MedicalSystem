from sqlalchemy import  Column, Integer, String
from app.database import Base


class Status(Base):
    __tablename__ = "status"
    
    id = Column(Integer,primary_key=True)
    status = Column(String,nullable=False) 
    