from app.dao.base import BaseDAO
from app.doctors.models import Doctors


class DoctorsDAO(BaseDAO):
    model = Doctors