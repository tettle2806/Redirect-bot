from sqlalchemy import Integer, Text, ForeignKey, String, Boolean
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Message(Base):
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.telegram_id"))
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.telegram_id"))
    content: Mapped[str] = mapped_column(Text)


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    keyword: Mapped[str] = mapped_column(String(300), default=None, nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)


class Project(Base):
    project_name: Mapped[str] = mapped_column(String(32), default='New Project')
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.telegram_id"))
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.telegram_id"))
    status: Mapped[bool] = mapped_column(Boolean, default=False)

    def __str__(self):
        return f"{self.__class__.__name__}(project_id={self.project_id}, project_name={self.project_name!r})"

    def __repr__(self):
        return str(self)

class Chat(Base):
    telegram_id: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.telegram_id"))
    chat_name: Mapped[str] = mapped_column(String(32), unique=True)
    chat_type: Mapped[str] = mapped_column(String(32))

    def __str__(self):
        return f"{self.__class__.__name__}(chat_id={self.chat_id}, chat_name={self.chat_name!r})"

    def __repr__(self):
        return str(self)
