from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import BaseModel
from db.models.mixins import IDMixin, FilePathMixin


class AttachmentPost(BaseModel, IDMixin, FilePathMixin):
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"), nullable=False)

    post: Mapped["Post"] = relationship("Post", back_populates="attachments", foreign_keys="Post.id")
