from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin


class Message(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    replied_to_message_id: Mapped[int] = mapped_column(Integer, ForeignKey("messages.id"), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=True)
