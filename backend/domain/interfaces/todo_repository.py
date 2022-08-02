from abc import ABCMeta
from uuid import UUID

from ..todo import Todo


class TodoRepository(metaclass=ABCMeta):

    def get(
            self,
            uuid: UUID,
    ) -> Todo:
        raise NotImplemented

    def create(
            self,
            todo: Todo,
            user_uuid: UUID
    ) -> Todo:
        raise NotImplemented

    def update(
            self,
            todo: Todo,
    ) -> Todo:
        raise NotImplemented

    def delete(
            self,
            uuid: UUID,
    ) -> None:
        raise NotImplemented

    def get_all_for_user(
            self,
            user_uuid: UUID
    ) -> list[Todo]:
        raise NotImplemented
