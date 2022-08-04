from backend.interfaces.bcrypt_hash import BcryptHash
from backend.interfaces.jwt_token_service import JWTTokenService
from backend.interfaces.repository.tortoise import UserTortoiseRepository, TodoTortoiseRepository
from backend.services import UserCases, TodoCases


def create_user_repository() -> UserCases:
    hash_service = BcryptHash()
    token_service = JWTTokenService()
    repository = UserTortoiseRepository()
    return UserCases(
        hash_service=hash_service,
        repository=repository,
        token_service=token_service,
    )


def create_todo_repository() -> TodoCases:
    repository = TodoTortoiseRepository()
    return TodoCases(
        repository=repository
    )


user_cases = create_user_repository()
todo_cases = create_todo_repository()
