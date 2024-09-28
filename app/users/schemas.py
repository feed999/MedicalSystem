from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: str
    
    
    
class SUser(BaseModel):
    email: EmailStr
    password: str
    
    
class SUserUpdate(BaseModel):
    email: EmailStr = None
    password: str = None
    phone: str = None
    