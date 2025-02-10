import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ChatAdministratorRights
from dotenv import load_dotenv

from handlers.add_chats import router as add_chats_router
from handlers.redirect import router as redirect_router
from keyboards.reply import main_kb

# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=main_kb()
    )


from aiogram import F
from aiogram.filters import Command
from aiogram.types import (
    KeyboardButton as Button,
    KeyboardButtonRequestChat as RequestChat,
    KeyboardButtonRequestUser as RequestUser,
    Message,
    ReplyKeyboardRemove as KeyboardRemove,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


@dp.message(Command("id"))
async def get_id_handler(message: Message) -> None:
    await message.answer(f"Your ID: {message.from_user.id}")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(add_chats_router)
    dp.include_router(redirect_router)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
