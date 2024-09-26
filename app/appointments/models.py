from sqlalchemy import (Column, Date, ForeignKey, Integer,Time)
from sqlalchemy.orm import relationship

from app.database import Base


class Appointments(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id")) 
    doctor_id = Column(ForeignKey("doctors.id"))
    appointment_date = Column(Date,nullable=False)
    date_regist = Column(Time,nullable=False)
    
    doctor = relationship("Doctors",back_populates="appointment")
    user = relationship("Users",back_populates="appointment")
    
    
    def __str__(self):
        return f"Appointment: #{self.id}"
    
    
    