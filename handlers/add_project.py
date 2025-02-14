from aiogram import F, Router
from aiogram.types import CallbackQuery

from database.crud import create_project
from keyboards.inline import back_kb, project_menu

router = Router()


@router.callback_query(F.data == "add_project")
async def add_new_project(call: CallbackQuery):
    new_project = await create_project(call.from_user.id)
    await call.message.answer(
        f"Проект: <b>{new_project.project_name}</b>",
        reply_markup=project_menu(new_project.status, new_project.id),
    )
