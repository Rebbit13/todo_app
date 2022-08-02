class TodoAlreadyDoneError(Exception):
    pass


class TodoOwnerNotValid(Exception):
    pass


class TodoTitleNotValid(Exception):
    pass


class TodoTextNotValid(Exception):
    pass


class AlreadyHasOwnerError(Exception):
    pass
