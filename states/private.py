from aiogram.fsm.state import StatesGroup, State


class KeywordState(StatesGroup):
    keyword = State()
