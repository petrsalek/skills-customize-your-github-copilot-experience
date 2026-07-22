from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float


_DB: List[Item] = []
_NEXT_ID = 1


@app.get("/items", response_model=List[Item])
def list_items(limit: int = Query(10, ge=1, le=100)):
    return _DB[:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _DB:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global _NEXT_ID
    item.id = _NEXT_ID
    _NEXT_ID += 1
    _DB.append(item)
    return item


@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}
