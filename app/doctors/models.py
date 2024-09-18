from sqlalchemy import JSON, Column, Integer, String
from app.database import Base
class Doctors(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,nullable=False) #ForeignKey
    room_id = Column(Integer,nullable=False) #ForeignKey
    image_id = Column(Integer)
    specialization = Column(JSON,nullable=False)
