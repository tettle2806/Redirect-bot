from aiogram import F, Router
from aiogram.types import CallbackQuery

from keyboards.inline import back_kb

router = Router()


@router.callback_query(F.data == "instruction")
async def show_instruction(call: CallbackQuery):
    text = f"""
        📖 ИНСТРУКЦИЯ

Этот бот перенаправляет сообщения по заданным ключевым словам из различных
каналов и групп в собственную группу\n\n
Краткая инструкция

🔹 Создайте проект
🔹 Добавьте группу/канал отправителя, откуда вы будете получать сообщения.
🔹 Создайте свою группу/канал в Telegram. Добавьте ее в список получателя.
🔹 Добавьте подпись к сообщению, которое будет отправлено в ваш группу/канал.
    """
    await call.message.answer(text=text, reply_markup=back_kb())
    await call.message.delete()
