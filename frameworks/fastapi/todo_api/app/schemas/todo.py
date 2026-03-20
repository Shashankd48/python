from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

class TodoOut(BaseModel):
    id: str
    title: str
    description: Optional[str]
    completed: bool
