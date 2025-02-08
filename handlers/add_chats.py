from aiogram import Router, F
from aiogram.types import Message

from keyboards.inline import ease_link_kb

router = Router()

@router.message(F.text == "➕ Добавить бота")
async def reply_kb(message: Message):
    await message.answer("Отправьте мне ссылку на бота", reply_markup=ease_link_kb())