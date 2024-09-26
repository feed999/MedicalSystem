from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    
    first_name = Column(String,nullable=False) 
    last_name = Column(String,nullable=False) 
    email = Column(String,nullable=False) 
    phone = Column(String,nullable=False) 
    hashed_password = Column(String,nullable=False) 
    role = Column(ForeignKey("roles.id"))
    
    user_role =  relationship("Roles",back_populates="user")
    doctor = relationship("Doctors",back_populates="user")
    appointment = relationship("Appointments",back_populates="user")
    document = relationship("Documents",back_populates="user")
    record = relationship("Records",back_populates="user")
    
    
    def __str__(self):
        return f"User: #{self.id} {self.email}"
    

