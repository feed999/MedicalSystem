from app.dao.base import BaseDAO
from app.records.models import Records


class RecordsDAO(BaseDAO):
    model = Records