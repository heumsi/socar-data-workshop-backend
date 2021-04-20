from typing import List

from pydantic import BaseModel

from model import Item


class GetItemResponse(BaseModel):
    id: int
    name: str

    @classmethod
    def from_item(cls, item: Item) -> "GetItemResponse":
        return cls(id=item.id, name=item.name)


class GetItemsResponse(BaseModel):
    items: List[GetItemResponse]

    @classmethod
    def from_items(cls, items: List[Item]) -> "GetItemsResponse":
        return cls(items=[GetItemResponse.from_item(item) for item in items])


class CreateItemRequest(BaseModel):
    name: str


class CreateItemResponse(BaseModel):
    id: int
    name: str

    @classmethod
    def from_item(cls, item: Item) -> "CreateItemResponse":
        return cls(id=item.id, name=item.name)
