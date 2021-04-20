from typing import ClassVar, Dict, List, Optional

from model import Item


class ItemRepository:
    DEFAULT_MAX_ITEM_SIZE: ClassVar[int] = 100

    def __init__(self, max_item_size: Optional[int]) -> None:
        self.max_item_size = self.DEFAULT_MAX_ITEM_SIZE if max_item_size is None else max_item_size
        self._data: Dict[int, Item] = {
            1: Item(
                id=1,
                name="Bag",
            ),
            2: Item(
                id=2,
                name="Shoes",
            ),
        }
        self.next_id = 3

    def find_all(self) -> List[Item]:
        return list(self._data.values())

    def find_by_id(self, item_id: int) -> Item:
        return self._data[item_id]

    def save(self, item: Item) -> None:
        if self.current_items_num >= self.max_item_size:
            raise Exception("Item을 저장할 수 있는 공간이 꽉 찼습니다!")
        self._data[item.id] = item

    @property
    def current_items_num(self):
        return len(self._data)

    def get_next_id(self) -> int:
        return_value = self.next_id
        self.next_id += 1

        return return_value
