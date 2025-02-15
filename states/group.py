from aiogram.fsm.state import StatesGroup, State


class GroupState(StatesGroup):
    project_name = State()
