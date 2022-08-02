from uuid import UUID

from backend.domain import UserRepository, TodoRepository, User, Todo
from .exceptions import NotAnOwnerError


class UseCases:

    def __init__(
            self,
            user_repository: UserRepository,
            todo_repository: TodoRepository
    ):
        self.user_repository = user_repository
        self.todo_repository = todo_repository

    def create_todo(
            self,
            user: User,
            todo: Todo
    ) -> Todo:
        todo.set_owner(user)
        todo.validate()
        return self.todo_repository.create(todo)

    def set_todo_done(
            self,
            user: User,
            todo_uuid: UUID
    ) -> Todo:
        todo = self.todo_repository.get(todo_uuid)
        if user.uuid != todo.owner.uuid:
            raise NotAnOwnerError("User must be an owner to set todo done")
        todo.set_done()
        return self.todo_repository.update(todo)

    def get_todos(self, user: User) -> list[Todo]:
        return self.todo_repository.get_all_for_user(user.uuid)
