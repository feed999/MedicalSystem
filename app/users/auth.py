from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.exceptions import IncorrectEmailException, IncorrectPasswordException
from app.users.dao import UserDAO

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password)->bool:
    if "$2b$" in hashed_password:
        return pwd_context.verify(plain_password,hashed_password)
    return plain_password == hashed_password

def create_access_token(data:dict)->str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
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
        return IncorrectPasswordException 
    return user

async def authenticate_user_auth(email:EmailStr,password:str):
    user = await UserDAO.find_one_or_none(email=email)
    if not user:
        return False 
    if not verify_password(password,user.hashed_password):
        return False 
    return user

