from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.rooms.router  import router as router_rooms
from app.users.router import router as router_users
app = FastAPI()

app.include_router(router_users)
app.include_router(router_rooms)

@app.get('/api/doctors/')
def get_doctors(doctor_id: int,
                date_start:date,
                date_end:date,
                stars:Optional[int] = Query(None,ge=1,le=5)):
    return "asdasd" + str(doctor_id)

class SBooking(BaseModel):
    room_id:int
    date_from:int
    date_to:int
    


@app.post('/api/booking')
def add_bookings(booking:SBooking):
    pass