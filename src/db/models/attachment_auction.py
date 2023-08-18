from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from db.models.base import BaseModel
from db.models.mixins import IDMixin, FilePathMixin


class AttachmentAuction(BaseModel, IDMixin, FilePathMixin):
    auction_id: Mapped[int] = mapped_column(Integer, ForeignKey("auctions.id"), nullable=False)

    auction: Mapped["Auction"] = relationship("Auction", remote_side="attachments", foreign_keys="Auction.id")
