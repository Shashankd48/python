# app/main.py
from fastapi import FastAPI
from app.api.v1 import todos
from app.db.client import connect_to_mongo, close_mongo_connection

app = FastAPI(title="Todo API")

app.include_router(todos.router)

@app.on_event("startup")
async def startup():
    await connect_to_mongo(app)

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection(app)
