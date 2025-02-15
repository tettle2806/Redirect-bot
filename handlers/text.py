from aiogram import Router


router = Router()


@router.message()
async def message_handler(message):
    chat_id = message.chat.id





