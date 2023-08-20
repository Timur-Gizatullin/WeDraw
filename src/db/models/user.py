from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import CreatedAtMixin, FilePathMixin, IDMixin, UpdatedAtMixin


class User(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin, FilePathMixin):
    __allow_unmapped__ = True

    email: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(length=255), nullable=True, unique=True)
    password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    auctions: Mapped[list["Auction"]] = relationship(  # type: ignore # noqa: F821
        "Auction", back_populates="creator", foreign_keys="Auction.creator.id"
    )
    sent_messages: Mapped[list["Message"]] = relationship(  # type: ignore # noqa: F821
        "Message", back_populates="sender", foreign_keys="Message.sender_id"
    )
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="creator", foreign_keys="Post.creator_id")  # type: ignore # noqa: F821
    subscribers: Mapped[list["Subscriber"]] = relationship(  # type: ignore # noqa: F821
        "Subscriber", back_populates="creator", foreign_keys="Subscriber.creator_id"
    )
    subscriptions: Mapped[list["Subscriber"]] = relationship(  # type: ignore # noqa: F821
        "Subscriber", back_populates="subscriber", foreign_keys="Subscriber.subscriber_id"
    )
    chats: Mapped[list["Chat"]] = relationship("Chat", foreign_keys="Chat.user_id")  # type: ignore # noqa: F821
    replenishments: Mapped[list["Transaction"]] = relationship(  # type: ignore # noqa: F821
        "Transaction", back_populates="receiver", foreign_keys="Transaction.receiver_id"
    )
    withdrawals: Mapped[list["Transaction"]] = relationship(  # type: ignore # noqa: F821
        "Transaction", back_populates="sender", foreign_keys="Transaction.sender_id"
    )
