from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from container import Container
from req_res_objects import CreateItemRequest, CreateItemResponse, GetItemResponse, GetItemsResponse
from service import ItemService

router = APIRouter()


@router.get("items/{item_id}", status_code=status.HTTP_200_OK, response_model=GetItemResponse)
@inject
def get_item(
    item_id: int,
    item_service: ItemService = Depends(Provide[Container.item_service]),
):
    item = item_service.get_item(item_id)
    return GetItemResponse.from_item(item)


@router.get("/items", status_code=status.HTTP_200_OK, response_model=GetItemsResponse)
@inject
def get_items(
    item_service: ItemService = Depends(Provide[Container.item_service]),
):
    items = item_service.get_items()
    return GetItemsResponse.from_items(items)


@router.post("/items", status_code=status.HTTP_201_CREATED, response_model=CreateItemResponse)
@inject
def create_item(
    request: CreateItemRequest,
    item_service: ItemService = Depends(Provide[Container.item_service]),
):
    item = item_service.create_item(name=request.name)
    return CreateItemResponse.from_item(item)
