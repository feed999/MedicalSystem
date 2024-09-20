from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt
from pydantic import EmailStr
from app.config import settings
from app.exceptions import IncorrectEmailException, IncorrectPasswordException
from app.users.dao import UserDAO
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_password_hash(password:str)->str:
    print(1)
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password)->bool:
    print(1)
    if "$2b$" in hashed_password:
        return pwd_context.verify(plain_password,hashed_password)
    return plain_password == hashed_password

def create_access_token(data:dict)->str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=5)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(
        to_encode,settings.SECRET_KEY,settings.ALGORITHM
    )
    return encoded_jwt

async def authenticate_user(email:EmailStr,password:str):
    user = await UserDAO.find_one_or_none(email=email)
    if not user:
        return IncorrectEmailException 
    if not verify_password(password,user.hashed_password):
        print(3)
        
        return IncorrectPasswordException 
    return user

