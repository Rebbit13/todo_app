from abc import ABCMeta

from .user import User


class Auth(metaclass=ABCMeta):

    def validate(
            self,
            user: User,
            creds: str
    ) -> bool:
        raise NotImplemented
