from pydantic import BaseModel


class TodoCreateUpdate(BaseModel):
    title: str
    text: str
