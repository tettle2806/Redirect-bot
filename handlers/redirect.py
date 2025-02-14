from aiogram import Router, F, Bot
from aiogram.types import Message

chats = [-1002423502910, -1002388870808]
router = Router()


@router.message()
async def echo_handler(message: Message, bot: Bot) -> None:
    await message.answer(message.text)
    print(message)

