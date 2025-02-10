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
        url="http://t.me/redirect_m_bot?startgroup=30913&admin=is_anonymous=True%20can_manage_chat=True%20can_delete_messages=True%20can_manage_video_chats=True%20can_restrict_members=True%20can_promote_members=True%20can_change_info=True%20can_invite_users=True%20can_post_stories=True%20can_edit_stories=True%20can_delete_stories=True%20can_post_messages=True%20can_edit_messages=True%20can_pin_messages=True%20can_manage_topics=True",
    )
    builder.button(
        text="Получатель",
        callback_data="no",
        url="http://t.me/redirect_m_bot?startgroup=&admin=is_anonymous=True+can_manage_chat=True+can_delete_messages=True+can_manage_video_chats=True+can_restrict_members=True+can_promote_members=True+can_change_info=True+can_invite_users=True+can_post_stories=True+can_edit_stories=True+can_delete_stories=True+can_post_messages=True+can_edit_messages=True+can_pin_messages=True+can_manage_topics=True",
    )
    builder.adjust(1)
    return builder.as_markup()
