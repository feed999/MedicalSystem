from pydantic import BaseModel

class SRooms(BaseModel):
    id : int
    name : str
    floor : int
    capacity : int
    
    
    class Config:
      from_attributes = True