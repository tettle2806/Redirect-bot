from aiogram import Router, F
from aiogram.types import Message

from keyboards.reply import main_kb

router = Router()


@router.message(F.text == "ℹ️ Инструкция")
async def reply_kb(message: Message):
    await message.answer(f"Как начать пользоваться ботом?\n\n"
                         f"<b>1. Добавьте бота в ваши чаты.</b>\n"
                         f"<b>2. Выдайте админские права.</b>\n"
                         f"<b>3. Укажите отправителя.</b>\n"
                         f"<b>4. Укажите получателя.</b>\n"
                         f"<b>5. Добавьте фразу для пересылки.</b>\n"
                         f"<b>6. Начните пересылать сообщения.</b>\n",
                         reply_markup=main_kb())


@router.message(F.text == "🔧 Фраза")
async def test(message: Message, bot: F.Bot):
    if message.chat.type == "private":
        await message.answer("Private chat")
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        await message.answer("Group chat")
    else:
        await message.answer("Error")


@router.message(F.text == "🔐 Проверить права админа")
async def check_admin_rights(message: Message, bot: F.Bot):
    members = await bot.get_chat_administrators(chat_id=message.chat.id)
    print(members)
    await message.answer(f"Участники чата: {members}")