from app.dao.base import BaseDAO
from app.documents.models import Documents


class DocumentsDAO(BaseDAO):
    model = Documents