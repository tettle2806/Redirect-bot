from asyncio import run_coroutine_threadsafe

from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.util import await_only

from config.config import bot
from database.crud import get_projects_by_id, update_project_status, update_project_name
from keyboards.inline import (
    sender_receiver_kb,
    my_projects_kb,
    project_menu,
    back_to_project,
)
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


@router.callback_query(lambda call: call.data.startswith("project_"))
async def project(call: CallbackQuery):
    project_id = int(call.data.split("_")[1])
    project_info = await get_projects_by_id(project_id)
    await call.message.answer(
        f"Проект: <b>{project_info.project_name}</b>",
        reply_markup=project_menu(project_info.status, project_info.id),
    )
    await call.message.delete()


@router.callback_query(lambda call: call.data.startswith("on_"))
async def project_on(call: CallbackQuery, bot: Bot):
    project_id = int(call.data.split("_")[1])
    await update_project_status(project_id, False)
    project_info = await get_projects_by_id(project_id)
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=project_menu(project_info.status, project_id),
    )


@router.callback_query(lambda call: call.data.startswith("off_"))
async def project_off(call: CallbackQuery, bot: Bot):
    project_id = int(call.data.split("_")[1])
    await update_project_status(project_id, True)
    project_info = await get_projects_by_id(project_id)
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=project_menu(project_info.status, project_id),
    )


@router.callback_query(lambda call: call.data.startswith("changeprojectname_"))
async def change_project_name(call: CallbackQuery, state: FSMContext):
    project_id = int(call.data.split("_")[1])
    await call.message.answer(
        f"<b>📋 Переименовать проект</b>\n\n" f"👇 Введите новое имя проекта:",
        reply_markup=back_to_project(project_id),
    )
    await state.update_data(project_id=project_id)
    await state.set_state(GroupState.project_name)


@router.message(GroupState.project_name)
async def change_project_name(message: Message, state: FSMContext):
    project_id = await state.get_data()
    project_name = message.text
    await state.clear()
    await update_project_name(
        project_id=project_id["project_id"], project_name=project_name
    )
    project_info = await get_projects_by_id(project_id["project_id"])
    await message.answer("✅ Сохранено")
    await message.answer(
        f"Проект: <b>{project_info.project_name}</b>",
        reply_markup=project_menu(project_info.status, project_id["project_id"]),
    )

    await message.delete()
