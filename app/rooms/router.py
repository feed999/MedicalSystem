from fastapi import APIRouter, Depends

from app.rooms.dao import RoomsDAO
from app.rooms.schemas import SRooms
from app.tools.default_api_response import (default_api_response,
                                            default_api_response_success)
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/rooms",
    tags=["Кабинеты"],
    
)

@router.get("")
async def get_all_rooms(user:Users = Depends(get_current_user)):
    print(user.id,user.role,user.email)
    result = await RoomsDAO.find_all()
    return await default_api_response(message=result)
    

@router.get("/{rooms_id}")
async def get_room(rooms_id):
    result = await RoomsDAO.find_by_id(int(rooms_id))
    return await default_api_response(message=result)
    
@router.post("/")
async def add_rooms(users:Users = Depends(get_current_admin_user)):
    await RoomsDAO.add()
    return await default_api_response_success()
