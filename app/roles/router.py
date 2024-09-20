from fastapi import APIRouter, Depends, Request
from app.roles.dao import RolesDAO
from app.roles.schemas import SRoles
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users



router = APIRouter(
    prefix="/roles",
    tags=["Роли"],
)

@router.get("/all")
async def get_all_roles(user:Users = Depends(get_current_admin_user))->list[SRoles]:
    result = await RolesDAO.find_all()
    return result