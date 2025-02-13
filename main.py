import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv

from database.crud import insert_user, get_user
from handlers.text_h import router as add_chats_router
from handlers.redirect import router as redirect_router
from handlers.add_keyword import router as add_keyword_router
from handlers.group import router as group_router
from keyboards.reply import main_kb, check_admin_rights
from states.group import GroupState

# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    telegram_id = message.from_user.id
    user = await get_user(telegram_id=telegram_id)

    if message.chat.type == "private":
        if user:
            await message.answer(
                f"Привет, {html.bold(message.from_user.full_name)}. "
                f"Данный бот предназначен для пересылки сообщений с одного чата в другой!",
                reply_markup=main_kb(),
            )
        else:
            await insert_user(
                telegram_id=message.from_user.id, username=message.from_user.username
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


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(add_chats_router)
    dp.include_router(redirect_router)
    dp.include_router(add_keyword_router)
    dp.include_router(group_router)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
