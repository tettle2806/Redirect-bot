from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonRequestChat,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def ease_link_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Отправитель",
        callback_data="yes",
        url="tg://resolve?domain=redirect_m_bot&startgroup&admin=change_info+post_messages+edit_messages+pin_messages"
    )
    builder.button(
        text="Получатель",
        callback_data="no",
        url="tg://resolve?domain=redirect_m_bot&startgroup&admin=change_info+post_messages+edit_messages+pin_messages"
    )
    builder.adjust(1)
    return builder.as_markup()
