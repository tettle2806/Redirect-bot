import asyncio
import logging
import sys
from os import getenv

from aiogram import html, F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from database.crud import insert_user, get_user
from handlers.text_h import router as add_chats_router
from handlers.redirect import router as redirect_router
from handlers.add_keyword import router as add_keyword_router
from handlers.group import router as group_router
from keyboards.inline import main_kb
from states.group import GroupState


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext, bot:Bot) -> None:
    telegram_id = message.from_user.id
    user = await get_user(telegram_id=telegram_id)

    if message.chat.type == "private":
        if user:
            await bot.send_animation(
                telegram_id,
    "CgACAgQAAxkBAAICHmevC4rEx4aj_I-IvwX_XdrQaGfqAALyAgACHh8NU8Q9ccqBIvztNgQ",
                caption=f"👋 Привет, {html.bold(message.from_user.full_name)}.\n\n"
                f"Создай свою новостную ленту с помощью этого бота. "
                        f"Выбери интересные источники и бот перешлет их посты в твою группу/канал/форум.\n\n"
                        f"⚠️ При настройке бота читай инструкцию!",
                reply_markup=main_kb()
            )
        else:
            await insert_user(
                telegram_id=telegram_id, username=message.from_user.username
            )
            await message.answer(
                f"Привет, {html.bold(message.from_user.full_name)}. "
                f"Данный бот предназначен для пересылки сообщений с одного чата в другой!",
                reply_markup=main_kb(),
            )
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        if user:
            """
            Нужно написать функцию для добавления чата в бд
            """

    else:
        await message.answer("Error")
@router.callback_query(F.data == "menu")
async def show_menu(call: CallbackQuery) -> None:
    text = """
    👋 Привет! Создай свою новостную ленту с помощью этого бота. Выбери интересные источники и бот перешлет их посты в твою группу/канал/форум.
    """
    await call.message.answer(text , reply_markup=main_kb())



