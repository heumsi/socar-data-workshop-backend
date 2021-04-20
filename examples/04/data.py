from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str


items = {
    1: Item(
        id=1,
        name="Bag",
    ),
    2: Item(
        id=2,
        name="Shoes",
    ),
}


def generate_item_id():
    id = len(items) + 1
    while True:
        yield id
        id += 1


item_id_generator = generate_item_id()
