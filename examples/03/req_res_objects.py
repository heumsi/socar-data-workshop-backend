from pydantic import BaseModel


class CreateItemRequest(BaseModel):
    name: str


class CreateItemResponse(BaseModel):
    id: int
    name: str
