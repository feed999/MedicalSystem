
from sqlalchemy import MetaData
from app.database import Base, async_session_maker, engine
metadata = MetaData()
Base.metadata.drop_all(engine)  # Удалить все таблицы
Base.metadata.create_all(engine)  # Создать заново
