from fastapi import APIRouter, Depends

from app.roles.dao import RolesDAO
from app.roles.schemas import SRoles
from app.tools.default_api_response import default_api_response
from app.users.dependencies import get_current_admin_user
from app.users.models import Users

router = APIRouter(
    prefix="/roles",
    tags=["Роли"],
)

@router.get("/all")
async def get_all_roles(user:Users = Depends(get_current_admin_user)):
    result = await RolesDAO.find_all()
    return await default_api_response(message=result)
    