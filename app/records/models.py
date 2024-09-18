from sqlalchemy import JSON, Column, Integer, String,Enum,Text
from app.database import Base
class Records(Base):
    __table_name__ = "records"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,nullable=False) #ForeignKey
    doctor_id = Column(Integer,nullable=False) #ForeignKey
    room_id = Column(Integer,nullable=False) #ForeignKey
    appointment_id = Column(Integer,nullable=False) #ForeignKey
    diagnosis = Column(String,nullable=False) 
    treatment = Column(Text,nullable=False) 




