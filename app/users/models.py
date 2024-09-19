from sqlalchemy import  Column, ForeignKey, Integer, String,Enum
from app.database import Base


class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    
    first_name = Column(String,nullable=False) 
    last_name = Column(String,nullable=False) 
    email = Column(String,nullable=False) 
    phone = Column(String,nullable=False) 
    hashed_password = Column(String,nullable=False) 
    role = Column(ForeignKey("roles.id")) #

