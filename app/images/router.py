from fastapi import APIRouter, Depends, UploadFile
import shutil

from app.users.dependencies import get_current_admin_user
from app.users.models import Users
# from app.tasks.tasks import process_pic
router = APIRouter(
    prefix="/images",
    tags =["Загрузка картинок"]
)

@router.post("/doctors")
async def add_doctor_images(name_id:str,file:UploadFile,user:Users = Depends(get_current_admin_user)):
    im_path = f"app/static/{str(name_id)}.webp"
    with open(im_path,"wb+") as file_object:
        shutil.copyfileobj(file.file,file_object)
    # process_pic.delay(im_path)
    
    # with open(f"app/static/{name_id}.webp",'wb+') as file_object:
    #     shutil.copy(file.file,file_object)