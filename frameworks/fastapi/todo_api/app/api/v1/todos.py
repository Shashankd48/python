from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.todo import TodoCreate, TodoOut, TodoUpdate
from app.db.client import get_db_client
from app.repositories.todo_repo import TodoRepository

router = APIRouter(prefix="/todos", tags=["todos"])

async def get_repo():
    db_client = get_db_client()
    db = db_client["todo_db"]
    yield TodoRepository(db)

@router.post("/", response_model=TodoOut, status_code=201)
async def create_todo(payload: TodoCreate, repo: TodoRepository = Depends(get_repo)):
    doc = await repo.create(payload)
    return doc

@router.get("/", response_model=list[TodoOut])
async def list_todos(repo: TodoRepository = Depends(get_repo), skip: int = 0, limit: int = 50):
    return await repo.list(skip=skip, limit=limit)
# ... get by id, update, delete
