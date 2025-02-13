from aiogram import Router, F, Bot
from aiogram.types import Message

chats = [-1002423502910, -1002388870808]
router = Router()


# @router.message()
# async def echo_handler(message: Message, bot: Bot) -> None:
#     text = message.text + f"\n\nОтправлено от @{message.from_user.username}"
#     user = message.from_user.username
#     chat_id = message.chat.id
#     print(f"Got message: {text} from chat: {chat_id}")
#     if chat_id == chats[0]:
#         await bot.send_message(text=text, chat_id=chats[1])
