from sqlalchemy import select

from database.db_helper import db_helper
from database.models import User


async def select_telegram_id_by_phone(phone: str):
    async with db_helper.session_factory() as session:
        stmt = select(User.telegram_id).where(User.phone_number == phone)
        telegram_id = await session.scalar(stmt)
        return telegram_id