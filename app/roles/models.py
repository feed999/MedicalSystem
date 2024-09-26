from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Roles(Base):
    __tablename__ = "roles"
    
    id = Column(Integer,primary_key=True)
    role = Column(String,nullable=False) 
    user = relationship("Users",back_populates="user_role")
    
    def __str__(self):
        return f"Role: {self.role}"