from sqlalchemy import JSON, Column, Integer, String
from app.database import Base
class Rooms(Base):
    __table_name__ = "rooms"
    
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False) 
    floor = Column(Integer,nullable=False)
    capacity = Column(Integer,nullable=False)
    
