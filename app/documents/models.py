from sqlalchemy import JSON, Column, ForeignKey, Integer, String,Enum
from app.database import Base
from sqlalchemy.orm import relationship


class Documents(Base):
    __tablename__ = "documents"
    
    id = Column(Integer,primary_key=True)
    user_id = Column(ForeignKey("users.id"))#ForeignKey
    passport = Column(String,nullable=False) 
    snils = Column(String,nullable=False) 
    polis = Column(String,nullable=False)
    
    user = relationship("Users",back_populates="document")
    
    def __str__(self):
        return f"Documents: #{self.id}"
     

