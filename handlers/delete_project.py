from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database.crud import delete_project_by_id, get_projects_by_id
from keyboards.inline import delete_project_kb, project_menu, my_projects_kb

router = Router()


@router.callback_query(lambda call: call.data.startswith("deleteproject_"))
async def delete_project(call: F.CallbackQuery, state: FSMContext):
    project_id = int(call.data.split("_")[1])
    await call.message.answer(
        "Вы уверены, что хотите удалить проект?",
        reply_markup=delete_project_kb(project_id),
    )
    await call.message.delete()

@router.callback_query(lambda call: call.data.startswith("delete_yes_"))
async def delete_yes(call: CallbackQuery):
    project_id = int(call.data.split("_")[2])
    await delete_project_by_id(project_id)
    await call.message.delete()
    await call.message.answer("Проект удален", reply_markup=await my_projects_kb(telegram_id=call.from_user.id))



@router.callback_query(lambda call: call.data.startswith("delete_no_"))
async def delete_yes(call: CallbackQuery):
    project_id = int(call.data.split("_")[2])
    project_info = await get_projects_by_id(project_id)
    await call.message.answer(
        f"Проект: <b>{project_info.project_name}</b>",
        reply_markup=project_menu(project_info.status, project_info.id),
    )
    await call.message.delete()