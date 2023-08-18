from sqlalchemy.orm import Mapped, relationship

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin


class Chat(BaseModel, IDMixin, CreatedAtMixin):
    pass

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="chat", foreign_keys="Message.chat_id")