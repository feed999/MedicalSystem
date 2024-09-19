from sqlalchemy import  Column, Integer, String,Enum
from app.database import Base


class Roles(Base):
    __tablename__ = "roles"
    
    id = Column(Integer,primary_key=True)
    role = Column(String,nullable=False) 