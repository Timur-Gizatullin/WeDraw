from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin


class Subscriber(BaseModel, IDMixin, CreatedAtMixin):
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    subscriber_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
