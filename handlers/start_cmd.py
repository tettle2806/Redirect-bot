import asyncio
import logging
import sys
from os import getenv

from aiogram import html, F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from database.crud import (
    insert_user,
    get_user,
    update_sender_id,
    get_projects_by_id,
    update_receiver_id,
)
from handlers.add_keyword import router as add_keyword_router
from handlers.group import router as group_router
from keyboards.inline import main_kb
from states.group import GroupState


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext, bot: Bot) -> None:
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
                reply_markup=main_kb(),
            )
            await message.delete()
        else:
            await insert_user(
                telegram_id=telegram_id, username=message.from_user.username
            )
            await bot.send_animation(
                telegram_id,
                "CgACAgQAAxkBAAICHmevC4rEx4aj_I-IvwX_XdrQaGfqAALyAgACHh8NU8Q9ccqBIvztNgQ",
                caption=f"👋 Привет, {html.bold(message.from_user.full_name)}.\n\n"
                f"Создай свою новостную ленту с помощью этого бота. "
                f"Выбери интересные источники и бот перешлет их посты в твою группу/канал/форум.\n\n"
                f"⚠️ При настройке бота читай инструкцию!",
                reply_markup=main_kb(),
            )
            await message.delete()
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        if user:
            try:
                text = message.text.split("_")
                chat_type = text[3]
                user_id = text[4]
                project_id = int(text[5])
                group_id = message.chat.id
                chat_name = message.chat.title
                print(
                    f"chat_type: {chat_type}, user_id: {user_id}, project_id: {project_id}, group_id: {group_id}"
                )
                project_info = await get_projects_by_id(project_id)
                if chat_type == "sender":
                    await update_sender_id(
                        project_id=project_id, sender_id=group_id, sender_name=chat_name
                    )
                    await message.answer(
                        f"✅ Отправитель добавлен к проекту ⁨{project_info.project_name}⁩"
                    )
                elif chat_type == "receiver":
                    await update_receiver_id(
                        project_id=project_id,
                        recipient_id=group_id,
                        recipient_name=chat_name,
                    )
                    await message.answer(
                        f"✅ Получатель добавлен к проекту ⁨{project_info.project_name}⁩"
                    )
            except IndexError:
                await message.answer("Не удалось получить данные, следуйте инструкции!")
    else:
        await message.answer("Error")


@router.callback_query(F.data == "menu")
async def show_menu(call: CallbackQuery, bot: Bot) -> None:
    telegram_id = call.from_user.id
    await bot.send_animation(
        telegram_id,
        "CgACAgQAAxkBAAICHmevC4rEx4aj_I-IvwX_XdrQaGfqAALyAgACHh8NU8Q9ccqBIvztNgQ",
        caption=f"👋 Привет, {html.bold(call.message.from_user.full_name)}.\n\n"
        f"Создай свою новостную ленту с помощью этого бота. "
        f"Выбери интересные источники и бот перешлет их посты в твою группу/канал/форум.\n\n"
        f"⚠️ При настройке бота читай инструкцию!",
        reply_markup=main_kb(),
    )
    await call.message.delete()
