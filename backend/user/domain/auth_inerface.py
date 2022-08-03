from abc import ABCMeta


class Auth(metaclass=ABCMeta):

    async def validate(
            self,
            user_name: str,
            creds: str
    ) -> bool:
        raise NotImplemented
