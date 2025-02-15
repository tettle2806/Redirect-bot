from sqlalchemy import Integer, Text, ForeignKey, String, Boolean
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Message(Base):
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.id"))
    sender_id: Mapped[int] = mapped_column(Integer, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    keyword: Mapped[str] = mapped_column(String(100), nullable=True)


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str] = mapped_column(String(32))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)


class Project(Base):
    project_name: Mapped[str] = mapped_column(String(32), default="New Project")
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.telegram_id"))
    sender_id: Mapped[int] = mapped_column(Integer, nullable=True)
    sender_name: Mapped[str] = mapped_column(String(32), nullable=True)
    recipient_id: Mapped[int] = mapped_column(Integer, nullable=True)
    recipient_name: Mapped[str] = mapped_column(String(32), nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    keyword: Mapped[str] = mapped_column(String(100), default=None, nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__}(project_id={self.id}, project_name={self.project_name!r})"

    def __repr__(self):
        return str(self)


class Chat(Base):
    chat_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_name: Mapped[str] = mapped_column(String(32))
    chat_type: Mapped[str] = mapped_column(String(32))
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.id"))

    def __str__(self):
        return f"{self.__class__.__name__}(chat_id={self.chat_id}, chat_name={self.chat_name!r})"

    def __repr__(self):
        return str(self)
