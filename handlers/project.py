from asyncio import run_coroutine_threadsafe

from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.util import await_only

from config.config import bot
from database.crud import get_projects_by_id, update_project_status
from keyboards.inline import sender_receiver_kb, my_projects_kb, project_menu
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
async def add_project(call: CallbackQuery):
    if call.message.chat.type == "private":
        await call.message.answer(
            "➕ Добавить проект",
            reply_markup=sender_receiver_kb(user_id=call.from_user.id),
        )
        await call.message.delete()
    else:
        await call.answer("Эту команду можно использовать только в личных сообщениях!")


@router.callback_query(lambda call: call.data.startswith("project_"))
async def project(call: CallbackQuery):
    project_id = int(call.data.split("_")[1])
    project_info = await get_projects_by_id(project_id)
    print(project_info)
    await call.message.answer(
        f"Проект: <b>{project_info.project_name}</b>",
        reply_markup=project_menu(project_info.status, project_info.id),
    )
    await call.message.delete()


@router.callback_query(lambda call: call.data.startswith("on_"))
async def project_on(call: CallbackQuery, bot: Bot):
    project_id = int(call.data.split("_")[1])
    project_info = await get_projects_by_id(project_id)
    await update_project_status(project_id, False)
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=project_menu(project_info.status, project_id),
    )


@router.callback_query(lambda call: call.data.startswith("off_"))
async def project_off(call: CallbackQuery, bot: Bot):
    project_id = int(call.data.split("_")[1])
    project_info = await get_projects_by_id(project_id)
    await update_project_status(project_id, True)
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=project_menu(project_info.status, project_id),
    )
