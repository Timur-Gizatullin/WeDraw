from pydantic import BaseModel, ConfigDict


class BaseOrmSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
