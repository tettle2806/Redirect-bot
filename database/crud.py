from sqlalchemy import select, update

from database.db_helper import db_helper
from database.models import User, Project


async def get_user(telegram_id: int):
    async with db_helper.session_factory() as session:
        stmt = select(User).where(User.telegram_id == telegram_id)
        user = await session.execute(stmt)
        user = user.fetchone()
        return user


async def insert_user(telegram_id: int, username: str):
    async with db_helper.session_factory() as session:
        user = User(telegram_id=telegram_id, username=username)
        session.add(user)
        await session.commit()
        return user


async def update_keyword(telegram_id: int, keyword: str):
    async with db_helper.session_factory() as session:
        stmt = (
            update(Project)
            .where(User.telegram_id == telegram_id)
            .values(keyword=keyword)
        )
        await session.execute(stmt)
        await session.commit()


async def get_projects_by_telegram_id(telegram_id: int):
    async with db_helper.session_factory() as session:
        stmt = select(Project).where(Project.owner_id == telegram_id)
        projects = await session.execute(stmt)
        projects = projects.fetchall()
        return projects
