from dataclasses import dataclass
from uuid import UUID

from .exceptions import TodoAlreadyDoneError
from .user import User


@dataclass
class Todo:
    uuid: UUID
    name: str
    text: str
    user: User
    done: bool

    def set_done(self):
        if self.done:
            raise TodoAlreadyDoneError("Todo is already done")
        self.done = True

    def check_if_owner(
            self,
            user: User
    ):
        return user.uuid == self.user.uuid
