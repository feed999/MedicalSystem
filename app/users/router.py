from fastapi import APIRouter, Depends, Response

from app.exceptions import *
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dao import UserDAO
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth
from app.validators.auth_validators import is_correct_email, is_correct_name, is_correct_password, is_correct_phone

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)

@router.post("/register")
async def register_user(user_data:SUserAuth):
    
    if not is_correct_email(user_data.email):
        raise IncorrectEmailException
    if not is_correct_password(user_data.password):
        raise IncorrectPasswordException
    if not is_correct_name(user_data.first_name):
        raise IncorrectFirstNameException
    if not is_correct_name(user_data.last_name):
        raise IncorrectLastNameException
    if not is_correct_phone(user_data.phone):
        raise IncorrectPhoneException

    existing_email = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_email:
        raise UserEmailAlreadyExistsException
    # if not existing_email:
    existing_phone = await UserDAO.find_one_or_none(phone=user_data.phone)
    if existing_phone:
        raise UserPhonelreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    # hashed_password = 'asdasdasd'
    await UserDAO.add(email=user_data.email, 
                      hashed_password=hashed_password,
                      first_name=user_data.first_name.capitalize(),
                      last_name=user_data.last_name.capitalize(),
                      phone=user_data.phone,
                      role=3
                      )
    
@router.post("/login")
async def login_user(response:Response,email:str,password:str):
    user = await authenticate_user(email, password)
    if user == IncorrectEmailException:
        raise IncorrectEmailException
    elif user == IncorrectPasswordException: 
        raise IncorrectPasswordException   
    access_token = create_access_token({"sub":str(user.id),"id":user.id,"role":user.role})
    response.set_cookie("user_access_token", access_token,httponly=True)
    
    return access_token


@router.post("/logout")
async def logout_user(response:Response):
    response.delete_cookie("user_access_token")
    return {"status":"success"}


@router.get("/me")
async def read_users_me(user:Users = Depends(get_current_user)):
    return user

@router.get("/all")
async def read_users_me(user:Users = Depends(get_current_admin_user)):
    return await UserDAO.find_all()

