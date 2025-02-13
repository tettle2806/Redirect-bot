from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonRequestChat,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def sender_receiver_btn(user_id):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Отправитель",
        callback_data="sender",
        url=f"tg://resolve?domain=redirect_m_bot&startgroup=sender{user_id}&admin=change_info+post_messages+edit_messages+pin_messages",
    )
    builder.button(
        text="Получатель",
        callback_data="receiver",
        url=f"tg://resolve?domain=redirect_m_bot&startgroup=receiver{user_id}&admin=change_info+post_messages+edit_messages+pin_messages",
    )
    builder.adjust(1)
    return builder.as_markup()


def add_captions():
    builtins = InlineKeyboardBuilder()
    builtins.button(text="🖍 Добавление подписи", callback_data="add_caption")
    builtins.adjust(1)
    return builtins.as_markup()
