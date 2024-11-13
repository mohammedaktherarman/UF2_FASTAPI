from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

items = {"arman": "arman"}

@app.get("/items/{item_id}", status_code=404)
async def read_item(item_id: str, response: Response):
    item = items.get(item_id)
    if item:
        return {"item_id": item_id} 
    response.status_code = 404
    return {"error": "Item not found"}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    country: str 
    day:str

@app.post("/items/")
async def create_item(item: Item):
    return item