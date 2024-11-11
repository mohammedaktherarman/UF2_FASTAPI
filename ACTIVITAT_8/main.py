from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

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