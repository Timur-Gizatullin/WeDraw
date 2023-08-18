from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin, FilePathMixin


class User(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin, FilePathMixin):
    __allow_unmapped__ = True

    email: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(length=255), nullable=True, unique=True)
    password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    auctions: Mapped[list["Auction"]] = relationship("Auction", back_populates="creator", foreign_keys="Auction.creator.id")
    sent_messages: Mapped[list["Message"]] = relationship("Message", back_populates="sender", foreign_keys="Message.sender_id")
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="creator", foreign_keys="Post.creator_id")
    subscribers: Mapped[list["Subscriber"]] = relationship("Subscriber", back_populates="creator", foreign_keys="Subscriber.creator_id")
    subscriptions: Mapped[list["Subscriber"]] = relationship("Subscriber", back_populates="subscriber",
                                                           foreign_keys="Subscriber.subscriber_id")
    chats: Mapped[list["Chat"]] = relationship("Chat", foreign_keys="Chat.user_id")
