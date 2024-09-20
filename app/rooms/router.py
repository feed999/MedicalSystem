from fastapi import APIRouter, Depends, Request
from app.rooms.dao import RoomsDAO
from app.rooms.schemas import SRooms
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users
router = APIRouter(
    prefix="/rooms",
    tags=["Кабинеты"],
    
)

@router.get("")
async def get_all_rooms(user:Users = Depends(get_current_user))->list[SRooms]:
    print(user.id,user.role,user.email)
    result = await RoomsDAO.find_all()
    # return {"rooms":result}
    return result
    

@router.get("/{rooms_id}")
async def get_room(rooms_id)->SRooms:
    result = await RoomsDAO.find_by_id(int(rooms_id))
    # return {"room":result}
    return result
    
@router.post("/")
async def add_rooms(
    users:Users = Depends(get_current_admin_user)
):
    await RoomsDAO.add()
# @router.get("/{rooms_id}")
# async def get_room_by_filter(rooms_id):
#     result = await RoomsDAO.find_one_or_none(id=2)
#     return {"room":result}