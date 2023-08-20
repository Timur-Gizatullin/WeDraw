from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import FilePathMixin, IDMixin


class AttachmentAuction(BaseModel, IDMixin, FilePathMixin):
    auction_id: Mapped[int] = mapped_column(Integer, ForeignKey("auctions.id"), nullable=False)

    auction: Mapped["Auction"] = relationship("Auction", remote_side="attachments", foreign_keys="Auction.id")  # type: ignore # noqa: F821
