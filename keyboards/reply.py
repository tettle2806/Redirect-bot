from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_kb(user_telegram_id: int = None):
    kb_list = [
        [KeyboardButton(text="➕ Добавить бота", url='https://t.me/redirect_m_bot?startgroup=start'), KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="📝 Заполнить анкету"), KeyboardButton(text="📚 Каталог")]
    ]
    # if user_telegram_id in admins:
    #     kb_list.append([KeyboardButton(text="⚙️ Админ панель")])
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard