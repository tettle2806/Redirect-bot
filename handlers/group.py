from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline import main_kb, sender_receiver_kb
from states.group import GroupState
from database.crud import get_projects_by_telegram_id, get_projects_by_id
router = Router()


@router.callback_query(lambda call: call.data.startswith("connectchats_"))
async def connect_chats(call: CallbackQuery):
    user_id = call.from_user.id
    project_id = int(call.data.split("_")[1])
    project_info = await get_projects_by_id(project_id)
    text = f"""
        🌐 Подключение чатов\n\n
📌 Для работы бота, добавьте данные чатов отправителя/получателя и предоставьте боту права администратора в чате получателя.\n\n
⚠️ Важно: В проекте допускается только один отправитель и один получатель. При возникновении проблем прочитайте инструкцию\n\n

Аккаунт пересылки: Системный

📤 Чат отправитель:
⁨{project_info.sender_name}⁩
--------------------
📥 Чат получатель:
⁨{project_info.recipient_name}⁩
    """
    await call.message.answer(text, reply_markup=sender_receiver_kb(project_id=project_id, user_id=user_id))