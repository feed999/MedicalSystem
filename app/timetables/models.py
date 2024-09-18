from sqlalchemy import JSON, Column, ForeignKey, Integer, String,Time
from app.database import Base
class Timetables(Base):
    __tablename__ = "timetables"
    
    id = Column(Integer,primary_key=True)
    doctor_id = Column(ForeignKey("doctors.id")) #ForeignKey
    available_from = Column(Time,nullable=False)
    available_to = Column(Time,nullable=False)
    