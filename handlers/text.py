from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery, Update

from database.crud import get_chats_by_chat_id, get_projects_by_id

router = Router()

@router.message(F.new_chat_members)
async def chat_join_request_handler(message: Message, bot: Bot):
    print("-------------------------")
    print(message.new_chat_members)
    print("-------------------------")


@router.message(F.message)
async def message_handler(message: Message, bot: Bot):
    if message.chat.type == "private":
        await message.answer("Не балуйся! 😊😊")
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        chat_id = message.chat.id
        chat_info = await get_chats_by_chat_id(chat_id)
        project_info = await get_projects_by_id(chat_info.project_id)
        if chat_info:
            if chat_info.chat_type == "sender" and project_info.status:
                if project_info.keyword:
                    text = f"{message.text}\n\n{project_info.keyword}"
                else:
                    text = message.text
                await bot.send_message(chat_id=project_info.recipient_id, text=text)
                await
        else:
            await message.answer("Группа не добавлена в проект! ????")
