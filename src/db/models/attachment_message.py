from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import FilePathMixin, IDMixin


class AttachmentMessage(BaseModel, IDMixin, FilePathMixin):
    message_id: Mapped[int] = mapped_column(Integer, ForeignKey("messages.id"), nullable=False)

    message: Mapped["Message"] = relationship("Message", back_populates="attachments", foreign_keys="Message.id")  # type: ignore # noqa: F821
