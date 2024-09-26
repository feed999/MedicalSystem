from fastapi import APIRouter, Depends

from app.timetables.dao import TimetablesDAO
from app.timetables.schemas import STimetables
from app.tools.default_api_response import default_api_response
from app.users.dependencies import  get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/timetables",
    tags=["Расписание"],
)

@router.get("/all")
async def get_all_timetables(user:Users = Depends(get_current_user)):
    result = await TimetablesDAO.find_all()
    return await default_api_response(message=result)


@router.get("/{doctor_id}")
async def get_all_timetables(doctor_id:int,user:Users = Depends(get_current_user)):
    result = await TimetablesDAO.find_one_or_none(doctor_id=doctor_id)
    return await default_api_response(message=result)



