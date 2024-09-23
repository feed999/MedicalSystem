from datetime import date, datetime,time
from pydantic import BaseModel

class SRecords(BaseModel):
    id:int
    user_id:str
    doctor_id:str
    appointment_id :int
    diagnosis:str
    treatment:str
    
    class Config:
      from_attributes = True