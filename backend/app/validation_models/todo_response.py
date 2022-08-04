from uuid import UUID

from pydantic import BaseModel


class TodoResponse(BaseModel):
    uuid: UUID
    title: str
    text: str
    done: bool
