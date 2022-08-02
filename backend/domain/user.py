from dataclasses import dataclass
from uuid import UUID

from .exceptions import UsernameNotValid

USERNAME_MAX_LENGTH = 100
USERNAME_MIN_LENGTH = 3


@dataclass
class User:
    username: str
    uuid: UUID | None = None

    def validate(self):
        if len(self.username) > USERNAME_MAX_LENGTH:
            raise UsernameNotValid(f"Username must be less than {USERNAME_MAX_LENGTH} chars")
        if len(self.username) < USERNAME_MIN_LENGTH:
            raise UsernameNotValid(f"Username must be more than {USERNAME_MIN_LENGTH} chars")
