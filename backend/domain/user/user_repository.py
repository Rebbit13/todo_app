from abc import ABCMeta
from uuid import UUID

from .user import User


class UserRepository(metaclass=ABCMeta):

    async def get(
            self,
            uuid: UUID = None,
            username: str = None,
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
