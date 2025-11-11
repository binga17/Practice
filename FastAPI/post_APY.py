from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []


class Item(BaseModel):
    name: str
    description: str
    
@app.post("/items/ ", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item
