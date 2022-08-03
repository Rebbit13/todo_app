from uuid import UUID

from backend.domain.todo import TodoRepository, Todo, Owner
from .models import TodoTortoise, UserTortoise


class TodoTortoiseRepository(TodoRepository):

    @staticmethod
    def _convert_to_domain_model(model: TodoTortoise) -> Todo:
        owner = Owner(
            uuid=model.owner_uuid
        )
        return Todo(
            uuid=model.uuid,
            owner=owner,
            done=model.done,
            title=model.title,
            text=model.text
        )

    async def get(
            self,
            uuid: UUID,
    ) -> Todo:
        todo = await TodoTortoise.get(uuid=uuid)
        return self._convert_to_domain_model(todo)

    async def create(
            self,
            todo: Todo,
    ) -> Todo:
        user = await UserTortoise.get(uuid=todo.owner.uuid)
        todo_to_create = TodoTortoise(
            title=todo.title,
            text=todo.text,
            owner=user
        )
        await todo_to_create.save()
        return self._convert_to_domain_model(todo_to_create)

    async def update(
            self,
            todo: Todo,
    ) -> Todo:
        todo_to_update = TodoTortoise(
            uuid=todo.uuid,
            title=todo.title,
            text=todo.text,
        )
        await todo_to_update.save()
        return self._convert_to_domain_model(todo_to_update)

    async def get_all_for_an_owner(
            self,
            user_uuid: UUID
    ) -> list[Todo]:
        todos = await TodoTortoise.filter(user_uuid=user_uuid)
        return [self._convert_to_domain_model(todo) for todo in todos]
