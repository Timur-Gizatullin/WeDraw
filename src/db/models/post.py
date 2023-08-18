from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import IDMixin, UpdatedAtMixin, CreatedAtMixin


class Post(BaseModel, IDMixin, UpdatedAtMixin, CreatedAtMixin):
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    creator: Mapped["User"] = relationship("User", back_populates="posts", foreign_keys="User.id")
