from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import CreatedAtMixin, IDMixin, UpdatedAtMixin


class Auction(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    actual_bet: Mapped[Decimal] = mapped_column(DECIMAL, nullable=False)
    last_bet_user_id: Mapped[int] = mapped_column(Integer, nullable=True)
    start_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finish_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    is_announce: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    creator: Mapped["User"] = relationship("User", back_populates="auctions", foreign_keys="User.id")  # type: ignore # noqa: F821
    attachments: Mapped["AttachmentAuction"] = relationship(  # type: ignore # noqa: F821
        "AttachmentAuction", back_populates="auction", foreign_keys="AttachmentAuction.auction_id"
    )
    last_bet_user: Mapped["User"] = relationship("User", back_populates="bets", foreign_keys="User.id")  # type: ignore # noqa: F821
