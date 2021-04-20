from repository import ItemRepository
from service import ItemService

item_repository = ItemRepository()
item_service = ItemService(item_repository=item_repository)
