from sqlalchemy import  Column, Integer, String,Enum
from app.database import Base

user_enum = Enum('ADMIN,', 'DOCTOR', 'PATIENT', name='user_enum_type')
class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    
    first_name = Column(String,nullable=False) 
    last_name = Column(String,nullable=False) 
    email = Column(String,nullable=False) 
    phone = Column(String,nullable=False) 
    hashed_password = Column(String,nullable=False) 
    role = Column(user_enum,nullable=False)

