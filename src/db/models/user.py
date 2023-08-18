from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin, FilePathMixin


class User(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin, FilePathMixin):
    __allow_unmapped__ = True

    email: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(length=255), nullable=True, unique=True)
    password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
