from sqlalchemy import JSON, Column, Integer, String,Time , Date,Enum
from app.database import Base
class Appointments(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,nullable=False) #ForeignKey
    doctor_id = Column(Integer,nullable=False) #ForeignKey
    room_id = Column(Integer,nullable=False) #ForeignKey
    appointment_date = Column(Date,nullable=False)
    date_regist = Column(Time,nullable=False)
    status = Column(Enum,nullable=False)
    