from sqlalchemy import JSON, Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Rooms(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False) 
    floor = Column(Integer,nullable=False)
    
    doctor = relationship("Doctors",back_populates="room")
    
    def __str__(self):
        return f"Room: {self.name}"
    
