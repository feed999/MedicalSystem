from sqlalchemy import (Column, Date, ForeignKey,
                        Integer, Time)
from sqlalchemy.orm import relationship

from app.database import Base


class Records(Base):
    __tablename__ = "records"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id")) 
    doctor_id = Column(ForeignKey("doctors.id"))
    appointment_date = Column(Date,nullable=False)
    date_regist = Column(Time,nullable=False)
    
    user = relationship("Users",back_populates="record")
    doctor = relationship("Doctors",back_populates="record")
    
        
    def __str__(self):
        return f"Record: #{self.id}"
    



