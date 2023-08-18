from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import IDMixin, FilePathMixin


class AttachmentMessage(BaseModel, IDMixin, FilePathMixin):
    message_id: Mapped[int] = mapped_column(Integer, ForeignKey("messages.id"), nullable=False)
