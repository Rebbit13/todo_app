from uuid import UUID

from backend.domain.todo import TodoRepository, Owner, Todo
from .exceptions import NotATodoRepository, NotAnOwnerError


class TodoCases:

    def __init__(
            self,
            repository: TodoRepository
    ):
        if not isinstance(repository, TodoRepository):
            raise NotATodoRepository("todo_repository must be instance of TodoRepository")
        self.todo_repository = repository

    async def create_todo(
            self,
            owner: Owner,
            todo: Todo
    ) -> Todo:
        todo.set_owner(owner)
        todo.validate()
        return await self.todo_repository.create(todo)

    async def change_todo(
            self,
            todo: Todo
    ) -> Todo:
        db_todo = await self.todo_repository.get(todo.uuid)
        for attr, value in todo.get_updated_dict().values():
            if value is not None:
                setattr(db_todo, attr, value)
        return await self.todo_repository.update(db_todo)

    async def set_todo_done(
            self,
            owner: Owner,
            todo_uuid: UUID
    ) -> Todo:
        todo = await self.todo_repository.get(todo_uuid)
        if owner.uuid != todo.owner.uuid:
            raise NotAnOwnerError("User must be an owner to set todo done")
        todo.set_done()
        return await self.todo_repository.update(todo)

    async def get_todos(self, owner: Owner) -> list[Todo]:
        return await self.todo_repository.get_all_for_an_owner(owner.uuid)
