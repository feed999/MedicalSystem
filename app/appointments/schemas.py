from datetime import date,time
from pydantic import BaseModel

class SAppointments(BaseModel):
    id:int
    user_id:int
    doctor_id:int
    status:int
    appointment_date:date
    date_regist:time
    
    class Config:
      from_attributes = True