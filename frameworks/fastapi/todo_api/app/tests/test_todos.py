# app/tests/test_todos.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_todo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/todos/", json={"title": "test"})
    assert r.status_code == 201
    assert r.json()["title"] == "test"
