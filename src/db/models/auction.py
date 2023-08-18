import decimal
from datetime import datetime

from sqlalchemy import Integer, ForeignKey, DECIMAL, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import UpdatedAtMixin, CreatedAtMixin, IDMixin


class Auction(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    actual_bet: Mapped[decimal] == mapped_column(DECIMAL, nullable=False)
    start_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finish_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    is_announce: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    creator: Mapped["User"] = relationship("User", back_populates="auctions", foreign_keys="User.id")
    attachments: Mapped["AttachmentAuction"] = relationship("AttachmentAuction", back_populates="auction", foreign_keys="AttachmentAuction.auction_id")
