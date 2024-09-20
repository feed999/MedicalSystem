from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.rooms.router  import router as router_rooms
from app.users.router import router as router_users
from app.timetables.router import router as router_timetables
from app.roles.router import router as router_roles
from app.documents.router import router as router_documents
from app.doctors.router import router as router_doctors
from app.appointments.router import router as router_appointments





app = FastAPI()

app.include_router(router_users)
app.include_router(router_rooms)
app.include_router(router_timetables)
app.include_router(router_roles)
app.include_router(router_documents)
app.include_router(router_doctors)

app.include_router(router_appointments)




# @app.get('/api/doctors/')
# def get_doctors(doctor_id: int,
#                 date_start:date,
#                 date_end:date,
#                 stars:Optional[int] = Query(None,ge=1,le=5)):
#     return "asdasd" + str(doctor_id)

