from sqlalchemy import JSON, Column, ForeignKey, Integer, String,Time , Date,Enum
from app.database import Base

class Appointments(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id")) #ForeignKey
    doctor_id = Column(ForeignKey("doctors.id")) #ForeignKey
    room_id = Column(ForeignKey("rooms.id")) #ForeignKey
    status = Column(ForeignKey("status.id"))
    appointment_date = Column(Date,nullable=False)
    date_regist = Column(Time,nullable=False)
    