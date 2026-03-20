from typing import List, Optional
from app.models.todo import TodoInDB
from app.schemas.todo import TodoCreate, TodoUpdate
from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorDatabase

class TodoRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.col = db.get_collection("todos")

    async def create(self, payload: TodoCreate) -> dict:
        res = await self.col.insert_one(payload.dict())
        return await self.col.find_one({"_id": res.inserted_id})

    async def get(self, _id) -> Optional[dict]:
        return await self.col.find_one({"_id": _id})

    async def list(self, skip: int = 0, limit: int = 50) -> List[dict]:
        cursor = self.col.find().skip(skip).limit(limit)
        return await cursor.to_list(length=limit)

    async def update(self, _id, payload: TodoUpdate):
        await self.col.update_one({"_id": _id}, {"$set": {k: v for k, v in payload.dict().items() if v is not None}})
        return await self.get(_id)

    async def delete(self, _id):
        await self.col.delete_one({"_id": _id})
        return True
