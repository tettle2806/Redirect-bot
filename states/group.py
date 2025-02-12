from aiogram.fsm.state import StatesGroup, State


class GroupState(StatesGroup):
    check_admin_rights = State()

    type_of_chat = State()
    sender = State()
    receiver = State()
    f5 = State()
