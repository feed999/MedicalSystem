
from datetime import datetime

from fastapi import Depends, Request
from jose import jwt

from app.config import settings
from app.exceptions import (TokenAbsentException, TokenAdminException,
                            TokenExpiredException)
from app.users.dao import UserDAO
from app.users.models import Users


def get_token(request:Request):
    token = request.cookies.get("user_access_token")
    if not token:
        print(0)
        
        raise TokenAbsentException
    return token

async def get_current_user(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(
        token,settings.SECRET_KEY,settings.ALGORITHM)
    except:
        print(1)
        raise TokenAbsentException
    expire :int = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        print(2)
        
        raise TokenExpiredException
    user_id:int =  payload.get("id")
    if not user_id:
        print(3)
        
        raise TokenAbsentException
    user = await UserDAO.find_by_id(user_id)
    if not user:
        print(4)
        
        raise TokenAbsentException
    return user

async def get_current_admin_user(user:Users = Depends(get_current_user)):
    if user.role !=1:
        raise TokenAdminException
    return user

async def get_current_doctor_user(user:Users = Depends(get_current_user)):
    if user.role !=2:
        raise TokenAdminException
    return user

async def get_current_admin(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(
        token,settings.SECRET_KEY,settings.ALGORITHM)
    except:
        raise TokenAbsentException
    expire :int = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise TokenExpiredException
    user_id:int =  payload.get("id")
    if not user_id:
        raise TokenAbsentException
    user = await UserDAO.find_by_id(user_id)
    if not user:
        raise TokenAbsentException
    if user.role !=1:
        raise TokenAdminException
    return user