from urllib.request import Request

from starlette.responses import JSONResponse

from backend.domain.todo import TodoAlreadyDoneError, TodoOwnerNotValid, TodoTitleNotValid, TodoTextNotValid, \
    AlreadyHasOwnerError
from backend.domain.user import UsernameNotValid, CredsNotValid
from backend.interfaces.exceptions import TokenExpired, TokenBroken
from backend.services import NotAuthorized, NotAnOwnerError


async def error_handling(request: Request, call_next):
    """ the middleware to handle all exceptions in app
    and convert it to a proper http response"""
    response = None
    try:
        response = await call_next(request)
    except TodoAlreadyDoneError as e:
        return JSONResponse({"message": e}, status_code=400)

    except TodoOwnerNotValid as e:
        return JSONResponse({"message": e}, status_code=400)

    except TodoTitleNotValid as e:
        return JSONResponse({"message": e}, status_code=400)

    except TodoTextNotValid as e:
        return JSONResponse({"message": e}, status_code=400)

    except AlreadyHasOwnerError as e:
        return JSONResponse({"message": e}, status_code=403)

    except UsernameNotValid as e:
        return JSONResponse({"message": e}, status_code=400)

    except CredsNotValid as e:
        return JSONResponse({"message": e}, status_code=400)

    except TokenExpired:
        return JSONResponse({"message": "Unauthorised"}, status_code=401)

    except TokenBroken:
        return JSONResponse({"message": "Unauthorised"}, status_code=401)

    except NotAuthorized:
        return JSONResponse({"message": "Unauthorised"}, status_code=401)

    except NotAnOwnerError as e:
        return JSONResponse({"message": e}, status_code=403)

    return response
