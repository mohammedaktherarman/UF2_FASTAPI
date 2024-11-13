from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {"arman": "arman"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

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