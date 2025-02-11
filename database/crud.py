from sqlalchemy import select

from database.db_helper import db_helper
from database.models import User


async def insert_user(telegram_id: int, username: str):
    async with db_helper.session_factory() as session:
        user = User(telegram_id=telegram_id, username=username)
        session.add(user)
        await session.commit()
        return user


async def update_keyword():
    async with db_helper.session_factory() as session:
        stmt = select(User).where(User.username == 'test')
        user = await session.execute(stmt)
        user = user.fetchone()
        user.keyword = 'test1'
        await session.commit()

