from datetime import date, datetime,time
from pydantic import BaseModel

class SRecords(BaseModel):
    id:int
    user_id:int
    doctor_id:int
    status_id:int
    appointment_id :int
    diagnosis:str
    treatment:str
    
    class Config:
      from_attributes = True