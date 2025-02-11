from aiogram.fsm.state import StatesGroup, State


class GroupState(StatesGroup):
    check_admin_rights = State()
    type_of_chat = State()
    f3 = State()
    f4 = State()
    f5 = State()
