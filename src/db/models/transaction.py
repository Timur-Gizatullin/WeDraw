from decimal import Decimal

from sqlalchemy import DECIMAL, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import CreatedAtMixin, IDMixin


class Transaction(BaseModel, IDMixin, CreatedAtMixin):
    sender_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(DECIMAL, nullable=False)

    sender: Mapped["User"] = relationship("User", back_populates="withdrawals", foreign_keys="User.id")  # type: ignore # noqa: F821
    receiver: Mapped["User"] = relationship("User", back_populates="replenishments", foreign_keys="User.id")  # type: ignore # noqa: F821
