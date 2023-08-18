from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin


class Chat(BaseModel, IDMixin, CreatedAtMixin):
    pass
