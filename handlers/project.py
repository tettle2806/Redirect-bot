from asyncio import run_coroutine_threadsafe

from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.util import await_only

from config.config import bot
from database.crud import get_projects_id
from keyboards.inline import sender_receiver_kb, my_projects_kb
from keyboards.inline import main_kb
from states.group import GroupState

router = Router()


@router.callback_query(F.data == "my_projects")
async def my_projects(call: CallbackQuery, state: FSMContext):
    if call.message.chat.type == "private":
        await call.message.answer(
            "📁 Мои проекты",
            reply_markup=await my_projects_kb(telegram_id=call.from_user.id),
        )
        await call.message.delete()
    else:
        await call.answer("Эту команду можно использовать только в личных сообщениях!")


@router.callback_query(F.data == "add_project")
async def add_project(call: CallbackQuery, state: FSMContext):
    if call.message.chat.type == "private":
        await call.message.answer(
            "➕ Добавить проект",
            reply_markup=sender_receiver_kb(user_id=call.from_user.id),
        )
        await call.message.delete()
    else:
        await call.answer("Эту команду можно использовать только в личных сообщениях!")


@router.callback_query(lambda call: call.data.startswith("project_"))
async def project(call: CallbackQuery, state: FSMContext):

    await call.message.answer(f"Вы выбрали проект с ID: {call.data}")



