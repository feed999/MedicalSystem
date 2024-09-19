from fastapi import APIRouter
from app.rooms.dao import RoomsDAO
from app.rooms.schemas import SRooms
router = APIRouter(
    prefix="/rooms",
    tags=["Кабинеты"],
    
)

@router.get("")
async def get_all_rooms()->list[SRooms]:
    result = await RoomsDAO.find_all()
    # return {"rooms":result}
    return result
    

@router.get("/{rooms_id}")
async def get_room(rooms_id)->SRooms:
    result = await RoomsDAO.find_by_id(int(rooms_id))
    # return {"room":result}
    return result
    

# @router.get("/{rooms_id}")
# async def get_room_by_filter(rooms_id):
#     result = await RoomsDAO.find_one_or_none(id=2)
#     return {"room":result}