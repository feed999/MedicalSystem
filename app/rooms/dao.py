from sqlalchemy import select
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.rooms.models import Rooms



class RoomsDAO(BaseDAO):
    model = Rooms
    
