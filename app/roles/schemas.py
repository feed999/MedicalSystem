from pydantic import BaseModel


class SRoles(BaseModel):
    id:int
    role:str

    class Config:
      from_attributes = True