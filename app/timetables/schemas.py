from pydantic import BaseModel

class STimetables(BaseModel):
    id : int
    doctor_id : int
    monday : list
    tuesday : list
    wednesday : list
    thursday : list
    friday : list
    
    
    class Config:
      from_attributes = True