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

from keyboards.reply import main_kb
from handlers.add_chats import router as add_chats_router
from handlers.redirect import router as redirect_router

# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


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
    kb = ReplyKeyboardBuilder()
    kb.row(
        Button(
            text="Chat",
            request_chat=RequestChat(
                request_id=1,
                chat_is_created=True,
                bot_is_member=True,
                chat_is_channel=False,
                user_administrator_rights=ChatAdministratorRights(
                    is_anonymous=True,
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_post_stories=True,
                    can_edit_stories=True,
                    can_delete_stories=True,
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_pin_messages=True,
                    can_manage_topics=True,
                ),
                bot_administrator_rights=ChatAdministratorRights(
                    is_anonymous=True,
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=True,
                    can_change_info=True,
                    can_invite_users=True,
                    can_post_stories=True,
                    can_edit_stories=True,
                    can_delete_stories=True,
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_pin_messages=True,
                    can_manage_topics=True,
                ),
            ),
        ),
        Button(
            text="Channel",
            request_chat=RequestChat(
                request_id=2,
                chat_is_channel=True,
            ),
        ),
    )
    kb.row(
        Button(
            text="User",
            request_user=RequestUser(
                request_id=3,
                user_is_bot=False,
            ),
        ),
        Button(
            text="Bot",
            request_user=RequestUser(
                request_id=4,
                user_is_bot=True,
            ),
        ),
    )
    await message.answer(
        "<b>Выберите кнопку для получения id:\n\n"
        "Для удаления клавиатуры -> /del</b>",
        reply_markup=kb.as_markup(resize_keyboard=True),
    )


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # dp.include_router(add_chats_router)
    # dp.include_router(redirect_router)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
