from fastapi import APIRouter, Depends, Response

from app.exceptions import *
from app.tools.default_api_response import (default_api_response,
                                            default_api_response_success)
from app.users.auth import (authenticate_user, create_access_token,
                            get_password_hash)
from app.users.dao import UserDAO
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users
from app.users.schemas import SUser, SUserAuth, SUserUpdate
from app.validators.auth_validators import (is_correct_email, is_correct_name,
                                            is_correct_password,
                                            is_correct_phone)

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
    existing_phone = await UserDAO.find_one_or_none(phone=user_data.phone)
    if existing_phone:
        raise UserPhonelreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(email=user_data.email, 
                      hashed_password=hashed_password,
                      first_name=user_data.first_name.capitalize(),
                      last_name=user_data.last_name.capitalize(),
                      phone=user_data.phone,
                      role=3)
    
    return await default_api_response_success()
    
    
@router.post("/login")
async def login_user(response:Response,user_data:SUser):
    user = await authenticate_user(user_data.email, user_data.password)
    if user == IncorrectEmailException:
        raise IncorrectEmailException
    elif user == IncorrectPasswordException: 
        raise IncorrectPasswordException   
    access_token = create_access_token({"sub":str(user.id),"id":user.id,"role":user.role})
    response.set_cookie("user_access_token", access_token,httponly=True)
    
    return await default_api_response_success()

@router.post("/update_data")
async def login_user(response:Response,user_data:SUserUpdate,user:Users = Depends(get_current_user)):
    # print(user.id)
    if user_data.email:
        if not is_correct_email(user_data.email):
            raise IncorrectEmailException
        existing_email = await UserDAO.find_one_or_none(email=user_data.email)
        if existing_email:
            raise UserEmailAlreadyExistsException
        await UserDAO.update_email(user_data.email,user.id)

    if user_data.password:
        if not is_correct_password(user_data.password):
            raise IncorrectPasswordException
        hashed_password = get_password_hash(user_data.password)
        await UserDAO.update_password(hashed_password,user.id)
        
    if user_data.phone:
        if not is_correct_phone(user_data.phone):
            raise IncorrectPhoneException
        existing_phone = await UserDAO.find_one_or_none(phone=user_data.phone)
        if existing_phone:
            raise UserPhonelreadyExistsException
        await UserDAO.update_phone(user_data.phone,user.id)

    return await default_api_response_success()


@router.post("/logout")
async def logout_user(response:Response):
    response.delete_cookie("user_access_token")
    return await default_api_response_success()



@router.get("/me")
async def read_users_me(user:Users = Depends(get_current_user)):
    return await default_api_response(message=user)


@router.get("/all")
async def read_users_me(user:Users = Depends(get_current_admin_user)):
    result = await UserDAO.find_all()
    return await default_api_response(message=result)

