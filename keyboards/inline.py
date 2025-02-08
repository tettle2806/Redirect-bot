from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonRequestChat,
)


def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Отправитель")],
        [KeyboardButtonRequestChat()],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
