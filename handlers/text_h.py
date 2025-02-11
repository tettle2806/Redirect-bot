from aiogram import Router, F
from aiogram.types import Message

from keyboards.reply import main_kb

router = Router()


@router.message(F.text == "ℹ️ Инструкция")
async def reply_kb(message: Message):
    await message.answer(f"Как начать пользоваться ботом?\n"
                         f"1. Добавьте бота в ваши чаты."
                         f"2. Выдайте админские права."
                         f"3. Укажите отправителя."
                         f"4. Укажите получателя."
                         f"5. Добавьте фразу для пересылки."
                         f"6. Начните пересылать сообщения.",
                         reply_markup=main_kb())


@router.callback_query(F.data == "test")
async def test(query, bot: F.Bot):
    await query.message.answer("Test")
    await bot.get_chat_member(query.message.chat.id, query.from_user.id)
