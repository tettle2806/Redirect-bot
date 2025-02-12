from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonRequestChat,
    ChatAdministratorRights,
)


def main_kb(user_telegram_id: int = None):
    kb_list = [
        [
            KeyboardButton(text="📁 Мои проекты"),
        ],
        [
            KeyboardButton(
                text="ℹ️ Инструкция",
            ),
            KeyboardButton(text="🔧 Фраза"),
        ],
        [
            KeyboardButton(text="📝 Отправить заявку"),
            KeyboardButton(text="📊 Статистика"),
        ],
    ]
    # if user_telegram_id in admins:
    #     kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:",
    )
    return keyboard


def check_admin_rights():
    kb_list = [
        [
            KeyboardButton(
                text="🔐 Проверить права админа",
            )
        ]
    ]
    # if user_telegram_id in admins:
    #     kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        input_field_placeholder="Че брат как дела?",
    )
    return keyboard


def type_of_chat():
    kb_list = [
        [
            KeyboardButton(
                text="📤 Отправитель",
            ),
            KeyboardButton(text="📥 Получатель"),
        ]
    ]
    # if user_telegram_id in admins:
    #     kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Одно из двух братан",
    )
    return keyboard
