from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.reply import main_kb, type_of_chat
from states.group import GroupState

router = Router()


@router.message(GroupState.check_admin_rights)
async def check_admin_rights(message: Message, bot: Bot, state: FSMContext):
    members = await bot.get_chat_member(chat_id=message.chat.id, user_id=7984318197)
    if members.status == "administrator":
        await message.answer(f"Выберите статус чата:", reply_markup=type_of_chat())
        await state.set_state(GroupState.type_of_chat)
    else:
        await message.answer("У бота нету прав администратора!")
        await state.set_state(GroupState.check_admin_rights)


@router.message(GroupState.type_of_chat)
async def save_type_of_chat(message: Message, state: FSMContext):
    if message.text == "📥 Получатель":
        await message.answer("📤 Отправитель")
        await state.set_state(GroupState.sender)
    elif message.text == "📥 Получатель":
        await message.answer("📥 Получатель")
        await state.set_state(GroupState.receiver)