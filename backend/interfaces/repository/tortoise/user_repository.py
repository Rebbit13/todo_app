from uuid import UUID

from backend.domain.user import UserRepository, User
from .models import UserTortoise


class UserTortoiseRepository(UserRepository):

    @staticmethod
    def _convert_to_domain_model(model: UserTortoise) -> User:
        return User(
            uuid=model.uuid,
            username=model.username,
            creds=model.password
        )

    async def get(
            self,
            uuid: UUID = None,
            username: str = None,
    ) -> User:
        query = UserTortoise
        if uuid:
            query = query.filter(uuid=uuid)
        if username:
            query = query.filter(username=username)
        user = await query.first()
        return self._convert_to_domain_model(user)

    async def create(
            self,
            user: User,
    ) -> User:
        user = UserTortoise(
            username=user.username,
            password=user.creds
        )
        await user.save()
        return self._convert_to_domain_model(user)

    async def update(
            self,
            user: User,
    ) -> User:
        user = UserTortoise(
            uuid=user.uuid,
            username=user.username,
            password=user.creds
        )
        await user.save()
        return self._convert_to_domain_model(user)
