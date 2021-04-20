import uvicorn
from fastapi import FastAPI
from starlette import status

from data import Item, item_id_generator, items
from req_res_objects import CreateItemRequest, CreateItemResponse, GetItemResponse, GetItemsResponse

app = FastAPI()


@app.get("items/{item_id}", status_code=status.HTTP_200_OK, response_model=GetItemResponse)
def get_item(item_id: int):
    item = items[item_id]
    return GetItemResponse.from_item(item)


@app.get("/items", status_code=status.HTTP_200_OK, response_model=GetItemsResponse)
def get_items():
    items_ = list(items.values())
    return GetItemsResponse.from_items(items_)


@app.post("/items", status_code=status.HTTP_201_CREATED, response_model=CreateItemResponse)
def create_item(request: CreateItemRequest):
    item_id = next(item_id_generator)
    items[item_id] = Item(
        id=item_id,
        name=request.name,
    )

    return CreateItemResponse(id=item_id, name=request.name)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
