
from sqlalchemy import and_, cast, func, insert, or_, select, text
from app.dao.base import BaseDAO
from app.records.models import Records
from app.database import async_session_maker, engine

class RecordsDAO(BaseDAO):
    model = Records