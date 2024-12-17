# coding: utf_8

from fastapi import FastAPI

@app.get("/")
def index():
    return {"Hello": "World"}