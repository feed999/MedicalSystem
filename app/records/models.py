from sqlalchemy import JSON, Column, ForeignKey, Integer, String,Enum,Text,DateTime
from app.database import Base
class Records(Base):
    __tablename__ = "records"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id")) #ForeignKey
    doctor_id = Column(ForeignKey("doctors.id")) #ForeignKey
    room_id = Column(ForeignKey("rooms.id")) #ForeignKey
    appointment_id = Column(ForeignKey("appointments.id")) #ForeignKey
    diagnosis = Column(String,nullable=False) 
    treatment = Column(Text,nullable=False) 
    created_at = Column(DateTime,nullable=False) 



