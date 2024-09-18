from sqlalchemy import JSON, Column, Integer, String,Enum
from app.database import Base
class Documents(Base):
    __tablename__ = "documents"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,primary_key=True) #ForeignKey
    passport = Column(String,nullable=False) 
    snils = Column(String,nullable=False) 
    polis = Column(String,nullable=False)
     

