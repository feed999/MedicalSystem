from fastapi import APIRouter, Depends

from app.documents.dao import DocumentsDAO
from app.documents.schemas import SDocuments
from app.exceptions import (IncorrectExistsException,
                            IncorrectPassportException,
                            IncorrectPolisException, IncorrectSnilsException)
from app.tools.default_api_response import (default_api_response,
                                            default_api_response_success)
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users
from app.validators.data_validators import *

router = APIRouter(
    prefix="/documents",
    tags=["Документы"],
)

@router.get("/me")
async def get_documents_my(user:Users = Depends(get_current_user)):
    documents = await DocumentsDAO.find_one_or_none(user_id = user.id)
    if documents:
        result = await DocumentsDAO.find_by_id(user.id)
        return await default_api_response(message=result)
    return await default_api_response(message=None)

@router.get("/id/{user_id}")
async def get_documents_by_id(user_id:int,user:Users = Depends(get_current_admin_user)):
    result = await DocumentsDAO.find_one_or_none(user_id=user_id)
    return await default_api_response(message=result)

@router.post("/add")
async def add_documents(
                passport: str,
                snils:str,
                polis:str,
                user:Users = Depends(get_current_user)):
    
    documents_exists = await DocumentsDAO.find_one_or_none(user_id=user.id)
    if documents_exists:
        raise IncorrectExistsException
    if not is_correct_passport(passport):
        raise IncorrectPassportException
    if not is_correct_snils(snils):
        raise IncorrectSnilsException
    if not is_correct_polis(polis):
        raise IncorrectPolisException

    await DocumentsDAO.add(user_id=user.id,passport = passport,snils=snils,polis=polis)
    return await default_api_response_success()


