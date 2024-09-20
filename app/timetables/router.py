from fastapi import APIRouter, Depends, Request
from app.timetables.dao import TimetablesDAO
from app.timetables.schemas import STimetables
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users



router = APIRouter(
    prefix="/timetables",
    tags=["Расписание"],
)

@router.get("/all")
async def get_all_timetables(user:Users = Depends(get_current_user))->list[STimetables]:
    result = await TimetablesDAO.find_all()
    # return {"rooms":result}
    return result

@router.get("/{doctor_id}")
async def get_all_timetables(doctor_id:int,user:Users = Depends(get_current_user)):
    result = await TimetablesDAO.find_by_id(doctor_id)
    # return {"rooms":result}
    return result

# @router.post("/add")
# async def add(doctor_id:int,user:Users = Depends(get_current_user)):
#     result = await TimetablesDAO.find_by_id(doctor_id)
#     # return {"rooms":result}
#     return result