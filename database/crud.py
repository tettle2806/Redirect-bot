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


async def get_projects_by_id(project_id: int) -> Project:
    async with db_helper.session_factory() as session:
        stmt = select(Project).where(Project.id == project_id)
        projects = await session.execute(stmt)
        projects = projects.scalar()
        return projects


async def create_project(owner_id: int):
    async with db_helper.session_factory() as session:
        project = Project(owner_id=owner_id)
        session.add(project)
        await session.commit()
        return project


async def update_project_status(project_id: int, status: bool):
    async with db_helper.session_factory() as session:
        stmt = update(Project).where(Project.id == project_id).values(status=status)
        await session.execute(stmt)
        await session.commit()


async def update_project_name(project_id: int, project_name: str):
    async with db_helper.session_factory() as session:
        stmt = (
            update(Project)
            .where(Project.recipient_id == project_id)
            .values(project_name=project_name)
        )
        await session.execute(stmt)
        await session.commit()


async def delete_project_by_id(project_id: int):
    async with db_helper.session_factory() as session:
        stmt = select(Project).where(Project.id == project_id)
        project = await session.execute(stmt)
        project = project.scalar()
        await session.delete(project)
        await session.commit()
        return project

async def update_sender_id(project_id: int, sender_id: int, sender_name: str):
    async with db_helper.session_factory() as session:
        stmt = (
            update(Project)
            .where(Project.id == project_id)
            .values(
                sender_id=sender_id,
                sender_name=sender_name
                    )
        )
        await session.execute(stmt)
        await session.commit()


async def update_receiver_id(project_id: int, recipient_id: int, recipient_name: str):
    async with db_helper.session_factory() as session:
        stmt = (
            update(Project)
            .where(Project.id == project_id)
            .values(
                recipient_id=recipient_id,
                recipient_name=recipient_name,
            )
        )
        await session.execute(stmt)
        await session.commit()
