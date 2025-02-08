from aiogram import Router, F, Bot
from aiogram.types import Message
from keyboards.inline import ease_link_kb
chats = [-1002389454663, -1002323150419]
router = Router()
@router.message()
async def echo_handler(message: Message, bot: Bot) -> None:
    text = message.text
    chat_id = message.chat.id
    print(f"Got message: {text} from chat: {chat_id}")
    if chat_id == chats[0]:
        await bot.send_message(text=text, chat_id=chats[1])
