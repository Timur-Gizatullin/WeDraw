from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin


class Message(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    chat_id: Mapped[int] = mapped_column(Integer, ForeignKey("chats.id"), nullable=False)
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    replied_to_message_id: Mapped[int] = mapped_column(Integer, ForeignKey("messages.id"), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=True)

    attachments: Mapped[list["AttachmentMessage"]] = relationship("AttachmentMessage", back_populates="message", foreign_keys="AttachmentMessage.chat_id")
    chat: Mapped["Chat"] = relationship("Chat", back_populates="messages", foreign_keys="Chat.id")
    sender: Mapped["User"] = relationship("User", back_populates="sent_messages", foreign_keys="User.id")
    replied_to_message: Mapped["Message"] = relationship("Message", remote_side="Message.id")
