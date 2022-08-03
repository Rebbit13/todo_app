from uuid import UUID

from backend.domain.todo import TodoRepository, User, Todo
from .exceptions import NotATodoRepository, NotAnOwnerError


class TodoCases:

    def __init__(
            self,
            repository: TodoRepository
    ):
        if not isinstance(repository, TodoRepository):
            raise NotATodoRepository("todo_repository must be instance of UserRepository")
        self.todo_repository = repository

    async def create_todo(
            self,
            user: User,
            todo: Todo
    ) -> Todo:
        todo.set_owner(user)
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
            user: User,
            todo_uuid: UUID
    ) -> Todo:
        todo = await self.todo_repository.get(todo_uuid)
        if user.uuid != todo.owner.uuid:
            raise NotAnOwnerError("User must be an owner to set todo done")
        todo.set_done()
        return await self.todo_repository.update(todo)

    async def get_todos(self, user: User) -> list[Todo]:
        return await self.todo_repository.get_all_for_user(user.uuid)
