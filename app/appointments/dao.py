from app.dao.base import BaseDAO
from app.appointments.models import Appointments


class AppointmentsDAO(BaseDAO):
    model = Appointments