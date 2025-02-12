from aiogram import Router, F
from aiogram.types import Message

from database.crud import update_keyword

router = Router()

@router.message(F.text == "🔧 Фраза")
async def add_keyword(message: Message):
    keyword = message.text
    telegram_id = message.from_user.id
    await update_keyword(keyword=keyword, telegram_id=telegram_id)
    await message.answer(f"Фраза успешно добавлена: {keyword}")