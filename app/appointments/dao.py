from datetime import date, time

from sqlalchemy import and_, func, insert, select, text

from app.appointments.models import Appointments
from app.dao.base import BaseDAO
from app.database import async_session_maker, engine


class AppointmentsDAO(BaseDAO):
    model = Appointments
    
    @classmethod
    async def add(
            cls,
            user_id:int,
            doctor_id:int,
            appointment_date:date,
            date_regist:time):
        """
        WITH app_records AS (
        SELECT * 
        FROM appointments
        WHERE 
            doctor_id = 1 
            AND 
            appointment_date = '2024-09-20'
        )
        SELECT COUNT(*) FROM app_records
        WHERE date_regist = '12:00:00'
        
        WHERE date_regist - '00:30:00'<= '12:00:00'
	or date_regist + '00:30:00' >= '12:00:00'
        """
        async with async_session_maker() as session:
            booked_appointment = select(Appointments).where(
                and_(
                    Appointments.doctor_id == doctor_id,
                    Appointments.appointment_date == appointment_date
                )
            ).cte("booked_appointment")
            
            query = (
                select(func.count())
                .select_from(booked_appointment)
                .where(
                     and_(    
                        booked_appointment.c.date_regist - text("interval '00:30:00'") < date_regist,
                        booked_appointment.c.date_regist + text("interval '00:30:00'") > date_regist
                        )
                       )
                )
            
            responce = await session.execute(query)
            appointment_exists = responce.scalar()
            
            if appointment_exists:
                return None
            add_appointment = insert(Appointments).values(
                user_id = user_id,
                doctor_id = doctor_id,
                appointment_date = appointment_date,
                date_regist = date_regist
                ).returning(Appointments)
            new_appointment = await session.execute(add_appointment)
            await session.commit()
            return new_appointment.scalar()
            