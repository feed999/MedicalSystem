from app.dao.base import BaseDAO
from app.doctors.models import Doctors
from sqlalchemy import and_, func, insert, select, text, update
from app.database import async_session_maker, engine

from app.rooms.models import Rooms
from app.users.models import Users


class DoctorsDAO(BaseDAO):
    model = Doctors
    
    
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = (
                select(
                    Doctors.id,
                    Users.first_name,
                    Users.last_name,
                    Rooms.name.label('room'),
                    Doctors.image_id,
                    Doctors.specialization,
                    Doctors.years_of_experience
                )
        .join(Rooms, Doctors.room_id == Rooms.id)
        .join(Users, Doctors.user_id == Users.id)
    )       
            result = await session.execute(query)
    # Используйте mappings() для получения результатов в виде словарей
            rows = result.mappings().all() 
            return rows 
                