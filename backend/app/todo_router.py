from uuid import UUID

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from backend.domain.user import User
from backend.domain.todo import Owner, Todo
from .oauth_scheme import get_current_user
from .app_constructor import todo_cases
from .validation_models import TodoResponse, TodoCreateUpdate

router = APIRouter(
    prefix="/todo",
    tags=["todo"]
)


@router.get("", response_model=list[TodoResponse])
async def get_all(current_user: User = Depends(get_current_user)):
    owner = Owner(uuid=current_user.uuid)
    return await todo_cases.get_todos(owner)


@router.post("", response_model=TodoResponse)
async def create(
        todo: TodoCreateUpdate,
        current_user: User = Depends(get_current_user)
):
    todo_to_create = Todo(
        owner=Owner(uuid=current_user.uuid),
        **todo.dict(exclude_unset=True)
    )
    todo = await todo_cases.create_todo(todo_to_create)
    return JSONResponse(
        status_code=201,
        content=todo
    )


@router.post("/{todo_uuid}/set_done", response_model=TodoResponse)
async def set_done(
        todo_uuid: UUID,
        current_user: User = Depends(get_current_user)
):
    owner = Owner(uuid=current_user.uuid)
    return await todo_cases.set_todo_done(owner, todo_uuid)


@router.patch("/{todo_uuid}", response_model=TodoResponse)
async def update(
        todo_uuid: UUID,
        todo: TodoCreateUpdate,
        current_user: User = Depends(get_current_user)
):
    todo_to_update = Todo(
        uuid=todo_uuid,
        owner=Owner(uuid=current_user.uuid),
        **todo.dict(exclude_unset=True)
    )
    return await todo_cases.change_todo(todo_to_update)
