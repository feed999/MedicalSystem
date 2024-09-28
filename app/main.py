from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin
from fastapi.middleware.cors import CORSMiddleware


from app.admin.auth import authentication_backend
from app.admin.views import (AppointmentsAdmin, DoctorsAdmin, DocumentsAdmin,
                             RecordsAdmin, RolesAdmin, RoomsAdmin,
                             TimetablesAdmin, UsersAdmin)

from app.appointments.router import router as router_appointments
from app.database import engine
from app.doctors.router import router as router_doctors
from app.documents.router import router as router_documents
from app.images.router import router as router_images
from app.records.router import router as router_records
from app.roles.router import router as router_roles
from app.rooms.router import router as router_rooms
from app.timetables.router import router as router_timetables
from app.users.router import router as router_users

app = FastAPI()


# Разрешенные домены
origins = [
    "http://localhost",  # Можно добавить конкретные домены
    "http://localhost:8000",
    "http://localhost:3000"
    
    # или "*" для разрешения всех доменов (не рекомендуется для продакшена)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Разрешенные источники
    allow_credentials=True,         # Разрешить куки и креденшелы
    allow_methods=["*"],            # Разрешить все методы
    allow_headers=["*"],            # Разрешить любые заголовки
)
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