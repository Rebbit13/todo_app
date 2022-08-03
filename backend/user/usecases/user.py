from .exceptions import NotAUserRepository, NotAnAuthService, NotAuthorized
from ..domain import UserRepository, Auth, User


class UseCases:

    def __init__(
            self,
            repository: UserRepository,
            auth: Auth,
    ):
        if not isinstance(repository, UserRepository):
            raise NotAUserRepository("repository must be instance of UserRepository")
        self.repository = repository

        if not isinstance(repository, Auth):
            raise NotAnAuthService("auth must instance of Auth")
        self.auth = auth

    def register(
            self,
            user: User
    ):
        user.validate()
        return await self.repository.create(user)

    def get_user(
            self,
            user: User
    ) -> User:
        if not await self.auth.validate(user.username, user.creds):
            raise NotAuthorized("User is not authorized")
        return await self.repository.get(user.uuid)
