import uvicorn
from fastapi import FastAPI

from data import items

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]


@app.get("/items")
def get_items():
    return {
        "items": list(items.values()),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
