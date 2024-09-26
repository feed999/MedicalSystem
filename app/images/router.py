import shutil

from fastapi import APIRouter, Depends, UploadFile

from app.tools.default_api_response import default_api_response_success
from app.users.dependencies import get_current_admin_user
from app.users.models import Users

router = APIRouter(
    prefix="/images",
    tags =["Загрузка картинок"]
)

@router.post("/doctors")
async def add_doctor_images(name_id:str,file:UploadFile,user:Users = Depends(get_current_admin_user)):
    im_path = f"app/static/{str(name_id)}.webp"
    with open(im_path,"wb+") as file_object:
        shutil.copyfileobj(file.file,file_object)
    return await default_api_response_success()
