from fastapi import APIRouter, Depends

from app.appointments.dao import AppointmentsDAO
from app.database import async_session_maker, engine
from app.doctors.dao import DoctorsDAO
from app.exceptions import (TokenAdminException)
from app.records.dao import RecordsDAO
from app.tools.default_api_response import (default_api_response,
                                            default_api_response_success)
from app.users.dependencies import (get_current_admin_user,
                                    get_current_doctor_user, get_current_user)
from app.users.models import Users

router = APIRouter(
    prefix="/records",
    tags=["История записей"],
)

@router.get("/all")
async def get_all_records(user:Users = Depends(get_current_admin_user)):
    result = await RecordsDAO.find_all()
    return await default_api_response(message=result)
    

@router.get("/my")
async def get_my_records(user:Users = Depends(get_current_user)):
    result = await RecordsDAO.find_one_or_none(user_id=user.id)
    return await default_api_response(message=result)
    


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
        
    await RecordsDAO.add(
        user_id = appointment.user_id,
        doctor_id = appointment.doctor_id,
        appointment_date = appointment.appointment_date,
        date_regist = appointment.date_regist
    )

    async with async_session_maker() as session:
        await session.delete(appointment)
        await session.commit()
        
    return await default_api_response_success()
    
