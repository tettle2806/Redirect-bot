from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline import sender_receiver_kb
from keyboards.inline import main_kb
from states.group import GroupState

router = Router()


@router.message(F.data == "📁 Мои проекты")
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