from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin


class Subscriber(BaseModel, IDMixin, CreatedAtMixin):
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    subscriber_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    creator: Mapped["User"] = relationship("User", back_populates="subscribers", foreign_keys="User.id")
    subscriber: Mapped["User"] = relationship("User", back_populates="subscriptions", foreign_keys="User.id")
