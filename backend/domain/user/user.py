from dataclasses import dataclass
from uuid import UUID

from .exceptions import UsernameNotValid, CredsNotValid


USERNAME_MAX_LENGTH = 100
USERNAME_MIN_LENGTH = 3


@dataclass
class User:
    username: str
    creds: str
    uuid: UUID = None

    def validate(self):
        if not isinstance(self.username, str):
            raise UsernameNotValid("Username must be string")
        if not USERNAME_MIN_LENGTH <= len(self.username) <= USERNAME_MAX_LENGTH:
            raise UsernameNotValid(
                f"Username must be more than {USERNAME_MIN_LENGTH} chars "
                f"and less than {USERNAME_MAX_LENGTH} chars"
            )

        if not isinstance(self.creds, str):
            raise UsernameNotValid("Creds must be string")
