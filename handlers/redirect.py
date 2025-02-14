from aiogram import Router, F, Bot
from aiogram.types import Message

chats = [-1002423502910, -1002388870808]
router = Router()


@router.message(F.animation)
async def redirect_animation(message: Message, bot: Bot):
    cid = message.animation.file_id
    await message.answer(f"ID: {cid}")
