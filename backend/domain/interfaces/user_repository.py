from abc import ABC
from uuid import UUID

from ..user import User


class TodoRepository(ABC):

    def get(
            self,
            uuid: UUID,
    ) -> User:
        raise NotImplemented

    def create(
            self,
            user: User,
    ) -> User:
        raise NotImplemented

    def update(
            self,
            user: User,
    ) -> User:
        raise NotImplemented

    def delete(
            self,
            uuid: UUID,
    ) -> None:
        raise NotImplemented
