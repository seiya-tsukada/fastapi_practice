# coding: utf_8

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "hello World"}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/")
async def read_item(item_id: int):
    return {"item_id": item_id}
