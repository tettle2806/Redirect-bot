from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.crud import update_keyword
from keyboards.inline import add_captions
from states.private import KeywordState

router = Router()


@router.message(F.text == "🖍 Добавление подписи")
async def add_keyword(message: Message, state: FSMContext):
    if message.chat.type == "private":

        await message.answer(
            f"🖍 Добавление подписи\n\n"
            f"Данная функция позволяет добавлять подписи в пересылаемые сообщения. "
            f"Можно вносить значения до 100 символов.:",
            reply_markup=add_captions(),
        )
        await state.set_state(KeywordState.keyword)
    else:
        await message.answer(
            "Эту команду можно использовать только в личных сообщениях!"
        )


@router.message(KeywordState.keyword)
async def add_keyword_in_db(message: Message):
    keyword = message.text
    telegram_id = message.from_user.id
    await update_keyword(keyword=keyword, telegram_id=telegram_id)
    await message.answer(f"Фраза <b>{keyword}</b> обновлена!")
