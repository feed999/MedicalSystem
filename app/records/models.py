from sqlalchemy import JSON, Column, Date, ForeignKey, Integer, String,Enum,Text,DateTime, Time
from app.database import Base
class Records(Base):
    __tablename__ = "records"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id")) #ForeignKey
    doctor_id = Column(ForeignKey("doctors.id")) #ForeignKey
    status = Column(ForeignKey("status.id"))
    appointment_date = Column(Date,nullable=False)
    date_regist = Column(Time,nullable=False)



