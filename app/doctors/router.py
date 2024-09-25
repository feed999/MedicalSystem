from fastapi import APIRouter, Depends

from app.doctors.dao import DoctorsDAO
from app.doctors.schemas import SDoctors
from app.users.dependencies import get_current_admin_user, get_current_user
from app.doctors.models import Doctors
from app.users.models import Users

router = APIRouter(
    prefix="/doctors",
    tags=["Доктора"],
)

@router.get("/all")
async def get_all_doctors(user:Users = Depends(get_current_user)):
    result = await DoctorsDAO.find_all()
    # return {"rooms":result}
    return result

@router.get("/{doctor_id}")
async def get_doctor(doctor_id:int,user:Users = Depends(get_current_user)):
    result = await DoctorsDAO.find_by_id(doctor_id)
    # return {"rooms":result}
    return result