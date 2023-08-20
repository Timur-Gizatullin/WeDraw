from sqlalchemy.orm import Mapped, relationship

from db.models.base import BaseModel
from db.models.mixins import CreatedAtMixin, IDMixin


class Chat(BaseModel, IDMixin, CreatedAtMixin):
    pass

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="chat", foreign_keys="Message.chat_id")  # type: ignore # noqa: F821
