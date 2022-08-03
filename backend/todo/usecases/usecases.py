from uuid import UUID

from ..domain import TodoRepository, User, Todo
from .exceptions import NotAnOwnerError, NotATodoRepository


class UseCases:

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
