from typing import List

from model import Item
from repository import ItemRepository


class ItemService:
    def __init__(self, item_repository: ItemRepository) -> None:
        self._item_repository = item_repository

    def get_items(self) -> List[Item]:
        items = self._item_repository.find_all()
        return items

    def get_item(self, item_id: int) -> Item:
        item = self._item_repository.find_by_id(item_id)
        return item

    def create_item(self, name: str) -> Item:
        item_id = self._item_repository.get_next_id()
        item = Item(id=item_id, name=name)
        self._item_repository.save(item)
        return item
