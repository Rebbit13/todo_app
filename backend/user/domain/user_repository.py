from abc import ABCMeta
from uuid import UUID

from .user import User


class UserRepository(metaclass=ABCMeta):

    async def get(
            self,
            uuid: UUID,
    ) -> User:
        raise NotImplemented

    async def create(
            self,
            user: User,
    ) -> User:
        raise NotImplemented

    async def update(
            self,
            user: User,
    ) -> User:
        raise NotImplemented

    async def delete(
            self,
            uuid: UUID,
    ) -> None:
        raise NotImplemented
