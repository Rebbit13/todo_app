from backend.domain import UserRepository, User


class UserCases:

    def __init__(
            self,
            repository: UserRepository
    ):
        self.repository = repository

    def create(
            self,
            user: User
    ):
        pass
