from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True


items = {
    1: Item(id=1, name="Sample Item", description="Starter item", price=9.99, in_stock=True).dict()
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API"}


@app.get("/items/", response_model=List[Item])
def list_items():
    return [Item(**v) for v in items.values()]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**items[item_id])


@app.post("/items/", status_code=201, response_model=Item)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items[item.id] = item.dict()
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.dict()
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
