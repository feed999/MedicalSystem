from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin, ModelView
from app.admin.views import AppointmentsAdmin, DoctorsAdmin, DocumentsAdmin, RecordsAdmin, RolesAdmin, RoomsAdmin, TimetablesAdmin, UsersAdmin
from app.database import engine
from app.rooms.router  import router as router_rooms
from app.users.models import Users
from app.users.router import router as router_users
from app.timetables.router import router as router_timetables
from app.roles.router import router as router_roles
from app.documents.router import router as router_documents
from app.doctors.router import router as router_doctors
from app.appointments.router import router as router_appointments
from app.records.router import router as router_records
from app.images.router import router as router_images
from app.admin.auth import authentication_backend
app = FastAPI()
app.mount('/static',StaticFiles(directory="app/static"),"static")

app.include_router(router_users)
app.include_router(router_rooms)
app.include_router(router_timetables)
app.include_router(router_roles)
app.include_router(router_documents)
app.include_router(router_doctors)
app.include_router(router_appointments)
app.include_router(router_records)
app.include_router(router_images)



admin = Admin(app,engine,authentication_backend=authentication_backend) 

admin.add_view(RolesAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(DocumentsAdmin)
admin.add_view(UsersAdmin)
admin.add_view(DoctorsAdmin)
admin.add_view(TimetablesAdmin)
admin.add_view(AppointmentsAdmin)
admin.add_view(RecordsAdmin)