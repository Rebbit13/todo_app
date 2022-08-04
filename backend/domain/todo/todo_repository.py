from abc import ABCMeta
from uuid import UUID

from .todo import Todo


class TodoRepository(metaclass=ABCMeta):

    async def get(
            self,
            uuid: UUID,
    ) -> Todo:
        raise NotImplemented

    async def create(
            self,
            todo: Todo,
    ) -> Todo:
        raise NotImplemented

    async def update(
            self,
            todo: Todo,
    ) -> Todo:
        raise NotImplemented

    async def get_all_for_an_owner(
            self,
            user_uuid: UUID
    ) -> list[Todo]:
        raise NotImplemented
