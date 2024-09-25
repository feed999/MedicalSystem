from sqlalchemy import JSON, Column, ForeignKey, Integer, String,Time,ARRAY
from app.database import Base
from sqlalchemy.orm import relationship

class Timetables(Base):
    __tablename__ = "timetables"
    
    id = Column(Integer,primary_key=True)
    doctor_id = Column(ForeignKey("doctors.id")) #ForeignKey
    monday = Column(ARRAY(Time),nullable=False)
    tuesday =Column(ARRAY(Time),nullable=False)
    wednesday = Column(ARRAY(Time),nullable=False)
    thursday = Column(ARRAY(Time),nullable=False)
    friday = Column(ARRAY(Time),nullable=False)
    
    doctor = relationship("Doctors",back_populates="timetables")
    
    def __str__(self):
        return f"Timetables: #{self.id} {self.doctor_id}"