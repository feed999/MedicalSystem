from datetime import date,time
from pydantic import BaseModel

class SAppointments(BaseModel):
    id:str
    user_id:str
    doctor_id:str
    status:str
    appointment_date:date
    date_regist:time
    
    class Config:
      from_attributes = True