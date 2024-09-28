from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.doctors.dao import DoctorsDAO
from app.tools.default_api_response import default_api_response
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/doctors",
    tags=["Доктора"],
)

@router.get("/all")
# async def get_all_doctors(user:Users = Depends(get_current_user)):
async def get_all_doctors():
    
    result = await DoctorsDAO.find_all()
    return await default_api_response(message=result)
@router.get("/{doctor_id}")
async def get_doctor(doctor_id:int,user:Users = Depends(get_current_user)):
    result = await DoctorsDAO.find_by_id(doctor_id)
    return await default_api_response(message=result)
    