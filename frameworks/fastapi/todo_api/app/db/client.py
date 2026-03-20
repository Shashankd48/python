# app/db/client.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

mongo_client: AsyncIOMotorClient | None = None

def get_db_client() -> AsyncIOMotorClient:
    assert mongo_client is not None, "Motor client not initialized"
    return mongo_client

async def connect_to_mongo(app):
    global mongo_client
    mongo_client = AsyncIOMotorClient(str(settings.MONGO_URI))
    # Optionally tune pool_size, timeouts, retryWrites, etc.
    app.state.mongo = mongo_client
    # ensure indexes
    db = mongo_client[settings.MONGO_DB]
    await db.todos.create_index("user_id")  # example
async def close_mongo_connection(app):
    mongo_client.close()
