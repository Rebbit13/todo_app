from abc import ABCMeta
from uuid import UUID

from ..user import User


class UserRepository(metaclass=ABCMeta):

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
