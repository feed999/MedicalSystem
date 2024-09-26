from sqlalchemy import  Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Doctors(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    room_id = Column(ForeignKey("rooms.id")) 
    image_id = Column(Integer)
    specialization = Column(String,nullable=False)
    years_of_experience = Column(Integer)
    about = Column(Text)
    
    room =  relationship("Rooms",back_populates="doctor")
    user = relationship("Users",back_populates="doctor")
    timetables = relationship("Timetables",back_populates="doctor")
    appointment = relationship("Appointments",back_populates="doctor")
    record = relationship("Records",back_populates="doctor")
    
    
    def __str__(self):
        return f"Doctor: #{self.id} {self.specialization}"
    