from sqlalchemy import JSON, Column, Date, ForeignKey, Integer, String,Enum,Text,DateTime, Time
from app.database import Base
from sqlalchemy.orm import relationship


class Records(Base):
    __tablename__ = "records"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id")) #ForeignKey
    doctor_id = Column(ForeignKey("doctors.id")) #ForeignKey
    appointment_date = Column(Date,nullable=False)
    date_regist = Column(Time,nullable=False)
    
    user = relationship("Users",back_populates="record")
    doctor = relationship("Doctors",back_populates="record")
    
        
    def __str__(self):
        return f"Record: #{self.id}"
    



