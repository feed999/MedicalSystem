from datetime import date, time
from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.appointments.dao import AppointmentsDAO
from app.appointments.models import Appointments
from app.doctors.dao import DoctorsDAO
from app.records.dao import RecordsDAO
from app.records.schemas import SRecords
from app.exceptions import AppointmentCannotBeRegister, RecordCannotBeRegister, TokenAdminException
from app.users.dependencies import get_current_admin_user, get_current_doctor_user, get_current_user
from app.records.models import Records
from app.users.models import Users
from app.database import async_session_maker, engine

router = APIRouter(
    prefix="/records",
    tags=["История записей"],
)

@router.get("/all")
async def get_all_records(user:Users = Depends(get_current_admin_user)):
    result = await RecordsDAO.find_all()
    # return {"rooms":result}
    return result

@router.get("/my")
async def get_my_records(user:Users = Depends(get_current_user)):
    result = await RecordsDAO.find_one_or_none(user_id=user.id)
    # return {"rooms":result}
    return result


@router.post("/add")
async def add_records(
                appointment_id: int,
                user:Users = Depends(get_current_doctor_user)):
    doctor = await DoctorsDAO.find_one_or_none(user_id=user.id)
    if not doctor:
        raise TokenAdminException
    appointment = await AppointmentsDAO.find_by_id(appointment_id)
    if appointment.doctor_id != doctor.id:
        raise TokenAdminException
        
    record = await RecordsDAO.add(
        user_id = appointment.user_id,
        doctor_id = appointment.doctor_id,
        appointment_date = appointment.appointment_date,
        date_regist = appointment.date_regist
    )

    async with async_session_maker() as session:
        await session.delete(appointment)
        await session.commit()
        
    return {"status":"success"}
