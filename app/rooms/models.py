from sqlalchemy import JSON, Column, Integer, String
from app.database import Base
class Rooms(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False) 
    floor = Column(Integer,nullable=False)
    
