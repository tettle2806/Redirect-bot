from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from database.crud import update_project_keyword
from keyboards.inline import back_to_project, my_projects_kb
from states.private import KeywordState

router = Router()


@router.callback_query(lambda call: call.data.startswith("add_caption_"))
async def add_caption(call: CallbackQuery, state: FSMContext):
    project_id = int(call.data.split("_")[2])
    await call.message.answer(
        f"<b>🖍 Добавление подписи</b>\n\n"
        f"Данная функция позволяет добавлять подписи в пересылаемые сообщения. "
        f"Можно вносить значения до 100 символов.\n\n",
        reply_markup=back_to_project(project_id),
    )
    await state.update_data(project_id=project_id)
    await state.set_state(KeywordState.keyword)


@router.message(state=KeywordState.keyword)
async def update_keyword(message: Message, state: FSMContext):
    data = await state.get_data()
    await update_project_keyword(project_id=data["project_id"], keyword=message.text)
    await state.clear()
    await message.answer(
        "Подпись успешно добавлена!",
        reply_markup=await my_projects_kb(message.from_user.id),
    )
