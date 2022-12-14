from dataclasses import dataclass
from uuid import UUID

from .exceptions import TodoAlreadyDoneError, TodoOwnerNotValid, TodoTitleNotValid, TodoTextNotValid, \
    AlreadyHasOwnerError
from .owner import Owner


TITLE_MAX_LENGTH = 100
TITLE_MIN_LENGTH = 3

TEXT_MAX_LENGTH = 300
TEXT_MIN_LENGTH = 3


@dataclass
class Todo:
    title: str = None
    text: str = None
    owner: Owner = None
    done: bool = False
    uuid: UUID | None = None

    def validate(self):
        # type checking
        if not isinstance(self.owner, Owner):
            raise TodoOwnerNotValid("Todo owner must be instance of User")
        if not isinstance(self.title, str):
            raise TodoTextNotValid("Todo title must be string")
        if not isinstance(self.text, str):
            raise TodoTitleNotValid("Todo text must be string")

        # length checking
        if not TITLE_MIN_LENGTH <= len(self.title) <= TITLE_MAX_LENGTH:
            raise TodoTitleNotValid(
                f"Todo title must be more than {TITLE_MIN_LENGTH} chars "
                f"and less than {TITLE_MAX_LENGTH} chars"
            )
        if not TEXT_MIN_LENGTH <= len(self.text) <= TEXT_MAX_LENGTH:
            raise TodoTextNotValid(
                f"Todo text must be more than {TEXT_MIN_LENGTH} chars "
                f"and less than {TEXT_MAX_LENGTH} chars"
            )

    def get_updated_dict(self) -> dict:
        """ returns dict with values that can be changed """
        return {
            "title": self.title,
            "text": self.text,
        }

    def set_done(self):
        if self.done:
            raise TodoAlreadyDoneError("Todo is already done")
        self.done = True

    def set_owner(self, owner: Owner):
        if self.owner:
            raise AlreadyHasOwnerError("Todo already has owner")
        self.owner = owner
