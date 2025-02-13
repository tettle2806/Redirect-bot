from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline import sender_receiver_kb
from keyboards.inline import main_kb
from states.group import GroupState

router = Router()


@router.callback_query(F.data == "📁 Мои проекты")
async def my_projects(message: Message, state: FSMContext):
    if message.chat.type == "private":
        await message.answer(
            "Ваши проекты:\n\n",
            reply_markup=sender_receiver_kb(user_id=message.from_user.id),
        )
    else:
        await message.answer(
            "Эту команду можно использовать только в личных сообщениях!"
        )


@router.message(F.text == "ℹ️ Инструкция")
async def reply_kb(message: Message):
    if message.chat.type == "private":
        await message.answer(
            f"Как начать пользоваться ботом?\n\n"
            f"<b>1. Добавьте бота в ваши чаты.</b>\n"
            f"<b>2. Выдайте админские права.</b>\n"
            f"<b>3. Укажите отправителя.</b>\n"
            f"<b>4. Укажите получателя.</b>\n"
            f"<b>5. Добавьте фразу для пересылки.</b>\n"
            f"<b>6. Начните пересылать сообщения.</b>\n",
            reply_markup=main_kb(),
        )
    else:
        await message.answer(
            "Эту команду можно использовать только в личных сообщениях!"
        )
