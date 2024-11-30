from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI is a Python class that provides all the functionality for your API.
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# Order matters
@app.get("/")
def read_root():
    return {"Hello": "World"}


# You can declare optional query parameters, by setting their default to None:
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
