from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.reply import main_kb, type_of_chat
from states.group import GroupState

router = Router()


