from sqlalchemy import JSON, Column, Integer, String,Enum
from app.database import Base
class Users(Base):
    __table_name__ = "users"
    
    id = Column(Integer,primary_key=True)
    
    first_name = Column(String,nullable=False) 
    last_name = Column(String,nullable=False) 
    email = Column(String,nullable=False) 
    phone = Column(String,nullable=False) 
    hash_password = Column(String,nullable=False) 
    role = Column(Enum,nullable=False)

