from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from app.database import Base
class Doctors(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id")) #ForeignKey
    room_id = Column(ForeignKey("rooms.id")) #ForeignKey
    image_id = Column(Integer)
    specialization = Column(String,nullable=False)
