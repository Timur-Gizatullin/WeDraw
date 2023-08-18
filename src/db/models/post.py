from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import IDMixin, UpdatedAtMixin, CreatedAtMixin


class Post(BaseModel, IDMixin, UpdatedAtMixin, CreatedAtMixin):
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    