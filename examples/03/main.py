import uvicorn
from fastapi import FastAPI

from data import item_id_generator, items
from req_res_objects import CreateItemRequest, CreateItemResponse

app = FastAPI()


@app.get("items/{item_id}")
def get_item(item_id: int):
    return items[item_id]


@app.get("/items")
def get_items():
    return {"items": list(items.values())}


@app.post("/items")
def create_item(request: CreateItemRequest):
    item_id = next(item_id_generator)
    items[item_id] = {
        "id": item_id,
        "name": request.name,
    }

    return CreateItemResponse(id=item_id, name=request.name)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
