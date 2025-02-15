from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButtonRequestChat,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.util import await_only

from database.crud import get_projects_by_telegram_id


def main_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="ℹ️ Инструкция",
        callback_data="instruction",
    )
    builder.button(text="📁 Мои проекты", callback_data="my_projects")
    builder.button(text="🖍 Добавление подписи", callback_data="add_caption")
    builder.button(text="📝 Отправить заявку", callback_data="send_request")
    builder.adjust(1)
    return builder.as_markup()


def sender_receiver_kb(user_id):
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


def add_captions_kb():
    builtins = InlineKeyboardBuilder()
    builtins.button(text="🖍 Добавление подписи", callback_data="add_caption")
    builtins.adjust(1)
    return builtins.as_markup()


async def my_projects_kb(telegram_id):
    button = InlineKeyboardButton(text="🏡 Меню", callback_data="menu")
    builtins = InlineKeyboardBuilder()
    projects = await get_projects_by_telegram_id(telegram_id)
    for project in projects:
        builtins.button(
            text=project[0].project_name, callback_data=f"project_{project[0].id}"
        )
    builtins.button(text="➕ Добавить проект", callback_data="add_project")
    builtins.adjust(2, 2)
    builtins.row(button)
    return builtins.as_markup()


def back_kb():
    builtins = InlineKeyboardBuilder()
    builtins.button(text="🏡 Меню", callback_data="menu")
    builtins.adjust(1)
    return builtins.as_markup()


def back_to_project(project_id: int):
    builtins = InlineKeyboardBuilder()
    builtins.button(text="<< Назад", callback_data=f"backtoproject_{project_id}")
    builtins.adjust(1)
    return builtins.as_markup()


def project_menu(status, project_id):
    if status:
        status = "🟢 Проект включен"
        data = "on"
    else:
        status = "🔴 Проект выключен"
        data = "off"
    builtins = InlineKeyboardBuilder()
    builtins.button(text=f"{status}", callback_data=f"{data}_{project_id}")
    builtins.button(
        text="🌐 Подключение чатов", callback_data=f"connectchats_{project_id}"
    )
    builtins.button(
        text="📋 Переименовать проект", callback_data=f"changeprojectname_{project_id}"
    )
    builtins.button(
        text="🗑️ Удалить проект", callback_data=f"deleteproject_{project_id}"
    )
    builtins.button(text="🏡 Меню", callback_data="menu")
    builtins.adjust(1)
    return builtins.as_markup()



def delete_project_kb(project_id):
    builtins = InlineKeyboardBuilder()
    builtins.button(text="✅ Да", callback_data=f"delete_yes_{project_id}")
    builtins.button(text="❌ Нет", callback_data=f"delete_no_{project_id}")
    builtins.adjust(1)
    return builtins.as_markup()
