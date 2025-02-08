from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonRequestChat,
    ChatAdministratorRights,
)


def main_kb(user_telegram_id: int = None):
    kb_list = [
        [
            KeyboardButton(
                text="➕ Добавить чат",
                request_chat=KeyboardButtonRequestChat(
                    request_id=1,
                    chat_is_channel=False,
                    bot_administrator_rights=ChatAdministratorRights(
                        is_anonymous=True,
                        can_manage_chat=True,
                        can_delete_messages=True,
                        can_manage_video_chats=True,
                        can_restrict_members=True,
                        can_promote_members=True,
                        can_change_info=True,
                        can_invite_users=True,
                        can_post_stories=True,
                        can_edit_stories=True,
                        can_delete_stories=True,
                        can_post_messages=True,
                        can_edit_messages=True,
                        can_pin_messages=True,
                        can_manage_topics=True,
                    ),
                ),
            ),
            KeyboardButton(text="👤 Профиль"),
        ],
        [KeyboardButton(text="📝 Заполнить анкету"), KeyboardButton(text="📚 Каталог")],
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
