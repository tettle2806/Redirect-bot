from aiogram import Router, F
from aiogram.types import Message

from keyboards.inline import ease_link_kb

router = Router()

@router.message(F.text == "➕ Добавить чат")
async def reply_kb(message: Message):
    await message.answer("Отправьте мне ссылку на бота", reply_markup=ease_link_kb())

@router.callback_query(F.data == "test")
async def test(query, bot: F.Bot):
    await query.message.answer("Test")
    await bot.get_chat_member(query.message.chat.id, query.from_user.id)