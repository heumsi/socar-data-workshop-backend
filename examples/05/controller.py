from fastapi import APIRouter
from starlette import status

from instances import item_service
from req_res_objects import CreateItemRequest, CreateItemResponse, GetItemResponse, GetItemsResponse

router = APIRouter()


@router.get("items/{item_id}", status_code=status.HTTP_200_OK, response_model=GetItemResponse)
def get_item(item_id: int):
    item = item_service.get_item(item_id)
    return GetItemResponse.from_item(item)


@router.get("/items", status_code=status.HTTP_200_OK, response_model=GetItemsResponse)
def get_items():
    items = item_service.get_items()
    return GetItemsResponse.from_items(items)


@router.post("/items", status_code=status.HTTP_201_CREATED, response_model=CreateItemResponse)
def create_item(request: CreateItemRequest):
    item = item_service.create_item(name=request.name)
    return CreateItemResponse.from_item(item)
