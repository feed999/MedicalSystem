from pydantic import BaseModel


class SDocuments(BaseModel):
    id : int
    user_id : int
    passport : str
    snils : str
    polis : str
    
    class Config:
      from_attributes = True