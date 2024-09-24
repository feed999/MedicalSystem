from datetime import date, time
from fastapi import APIRouter, Depends

from app.appointments.dao import AppointmentsDAO
from app.appointments.schemas import SAppointments
from app.doctors.dao import DoctorsDAO
from app.documents.dao import DocumentsDAO
from app.exceptions import AppointmentCannotBeRegister, IncorrectNotExistsException
from app.users.dependencies import get_current_admin_user, get_current_doctor_user, get_current_user
from app.appointments.models import Appointments
from app.users.models import Users
from app.users.schemas import SUserAuth

router = APIRouter(
    prefix="/appointments",
    tags=["Запись на прием"],
)

@router.get("/all")
async def get_all_appointments(user:Users = Depends(get_current_admin_user)):
    result = await AppointmentsDAO.find_all()
    # return {"rooms":result}
    return result

@router.get("/my")
async def get_my_appointments(user:Users = Depends(get_current_user),
                              appointment_id:int = None)->list[SAppointments]:
    if appointment_id:
        result = await AppointmentsDAO.find_all(id = appointment_id,user_id=user.id)
    else:
        result = await AppointmentsDAO.find_all(user_id=user.id)
        
    # return {"rooms":result}
    return result

@router.get("/by_doctor")
async def get_my_appointments(user:Users = Depends(get_current_doctor_user)):
    user = await DoctorsDAO.find_one_or_none(user_id=user.id)
    if user:
        result = await AppointmentsDAO.find_all(doctor_id=user.id)
        return result
    return None
        

@router.post("/add")
async def add_appointments(
                doctor_id: int,
                appointment_date:date,
                date_regist:time,
                user:Users = Depends(get_current_user)):
    documents_exists = await DocumentsDAO.find_one_or_none(user_id=user.id)
    if not documents_exists:
        raise IncorrectNotExistsException
    appointment = await AppointmentsDAO.add(user.id,doctor_id,appointment_date,date_regist)
    if not appointment:
        raise AppointmentCannotBeRegister