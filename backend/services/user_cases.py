from datetime import timedelta

from .exceptions import NotAuthorized, NotAHashInterface, NotAUserRepository
from .interfaces import HashInterface, TokenInterface, TokenType
from backend.domain.user import UserRepository, User


TOKEN_LIVING_TIME = timedelta(minutes=30)


class UserCases:

    def __init__(
            self,
            hash_service: HashInterface,
            repository: UserRepository,
            token_service: TokenInterface
    ):
        if not isinstance(hash_service, HashInterface):
            raise NotAHashInterface("hash_service must be instance of HashInterface")
        self.hash_service = hash_service
        if not isinstance(repository, UserRepository):
            raise NotAUserRepository("repository must be instance of UserRepository")
        self.repository = repository
        if not isinstance(token_service, TokenInterface):
            raise NotAUserRepository("token_service must be instance of TokenInterface")
        self.token_service = token_service

    def _create_token_pair(
            self,
            user_uuid
    ) -> (str, str):
        """ generates access and refresh tokens by uuid"""
        access = self.token_service.create_token(
            str(user_uuid),
            TokenType.access,
            TOKEN_LIVING_TIME
        )
        refresh = self.token_service.create_token(
            str(user_uuid),
            TokenType.refresh,
            TOKEN_LIVING_TIME + timedelta(minutes=3)
        )
        return access, refresh

    async def register(
            self,
            username: str,
            password: str
    ) -> User:
        password = self.hash_service.hash(password)
        user = User(username=username, creds=password)
        user.validate()
        return await self.repository.create(user)

    def change_password(
            self,
            username: str,
            old_password: str,
            new_password: str,
    ) -> User:
        user = await self.repository.get(username=username)
        if not self.hash_service.verify(old_password, user.creds):
            raise NotAuthorized("User is not authorized")
        user.creds = self.hash_service.hash(new_password)
        return await self.repository.update(user)

    def sign_in(
            self,
            username: str,
            password: str
    ) -> (str, str):
        """ returns access and refresh tokens """
        user = await self.repository.get(username=username)
        if not self.hash_service.verify(password, user.creds):
            raise NotAuthorized("User is not authorized")
        return self._create_token_pair(user.uuid)

    def authorize(
            self,
            access: str,
    ) -> User:
        payload = self.token_service.decode_access_token(access)
        if payload.token_type != TokenType.access:
            raise NotAuthorized("Token must be an access token")
        return await self.repository.get(uuid=payload.user_uuid)

    def refresh(
            self,
            refresh: str,
    ) -> (str, str):
        payload = self.token_service.decode_access_token(refresh)
        if payload.token_type != TokenType.refresh:
            raise NotAuthorized("Token must be a refresh token")
        user = await self.repository.get(uuid=payload.user_uuid)
        return self._create_token_pair(user.uuid)
