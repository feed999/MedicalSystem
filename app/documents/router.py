from fastapi import APIRouter, Depends

from app.documents.dao import DocumentsDAO
from app.documents.schemas import SDocuments
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/documents",
    tags=["Документы"],
)

@router.get("/me")
async def get_documents_my(user:Users = Depends(get_current_user)):
    result = await DocumentsDAO.find_one_or_none(user_id = user.id)
    if result:
        return await DocumentsDAO.find_by_id(user.id)
    return result
@router.get("/id/{user_id}")
async def get_documents_by_id(user_id:int,user:Users = Depends(get_current_admin_user))-> SDocuments:
    return await DocumentsDAO.find_one_or_none(user_id=user_id)

# @router.post("/add")
# async def get_documents_by_id(user_id:int,user:Users = Depends(get_current_admin_user))-> SDocuments:
#     return await DocumentsDAO.find_by_id(user_id)


