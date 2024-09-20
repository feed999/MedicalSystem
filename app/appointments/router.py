from fastapi import APIRouter, Depends

from app.appointments.dao import AppointmentsDAO
from app.appointments.schemas import SAppointments
from app.users.dependencies import get_current_admin_user, get_current_user
from app.appointments.models import Appointments
from app.users.models import Users

router = APIRouter(
    prefix="/appointments",
    tags=["Запись на прием"],
)

@router.get("/all")
async def get_all_doctors(user:Users = Depends(get_current_admin_user)):
    result = await AppointmentsDAO.find_all()
    # return {"rooms":result}
    return result

@router.get("/my")
async def get_all_doctors(user:Users = Depends(get_current_user)):
    result = await AppointmentsDAO.find_one_or_none(user_id=user.id)
    # return {"rooms":result}
    return result