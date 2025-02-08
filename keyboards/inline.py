from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Отправитель", url='https://t.me/redirect_m_bot?startgroup=start')],
        [InlineKeyboardButton(text="Получатель", url='http://t.me/redirect_m_bot?startgroup=30913&admin=is_anonymous=True%20can_manage_chat=True%20can_delete_messages=True%20can_manage_video_chats=True%20can_restrict_members=True%20can_promote_members=True%20can_change_info=True%20can_invite_users=True%20can_post_stories=True%20can_edit_stories=True%20can_delete_stories=True%20can_post_messages=True%20can_edit_messages=True%20can_pin_messages=True%20can_manage_topics=True',callback_data='test')],

    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)