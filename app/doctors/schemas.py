from pydantic import BaseModel

class SDoctors(BaseModel):
    user_id:int
    room_id:int
    image_id:int
    specialization:str
    
    class Config:
      from_attributes = True