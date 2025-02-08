from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from base import Base


class Message(Base):

    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    recipient_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    content: Mapped[str] = mapped_column(Text)
