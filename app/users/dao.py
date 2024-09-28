from sqlalchemy import update
from app.dao.base import BaseDAO
from app.users.models import Users
from app.database import async_session_maker, engine


class UserDAO(BaseDAO):
    model = Users
    
    
    
    @classmethod
    async def update_password(cls,new_password,user_id):
        async with async_session_maker() as session:
            query = (
                update(Users)
                .where(Users.id == user_id)
                .values(hashed_password=new_password)
            )
            await session.execute(query)
            await session.commit() 
    @classmethod
    async def update_email(cls,new_email,user_id):
        async with async_session_maker() as session:
            query = (
                update(Users)
                .where(Users.id == user_id)
                .values(email=new_email)
            )
            await session.execute(query)
            await session.commit() 
    @classmethod
    async def update_phone(cls,new_phone,user_id):
        async with async_session_maker() as session:
            query = (
                update(Users)
                .where(Users.id == user_id)
                .values(phone=new_phone)
            )
            await session.execute(query)
            await session.commit() 