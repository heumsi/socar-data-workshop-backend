from dependency_injector import containers, providers

from repository import ItemRepository
from service import ItemService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    item_repository = providers.Singleton(ItemRepository, max_item_size=config.item_repository.max_item_size)
    item_service = providers.Singleton(ItemService, item_repository=item_repository)
