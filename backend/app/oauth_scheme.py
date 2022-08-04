from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from backend.app.app_constructor import user_cases

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/sign_in")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    return await user_cases.authorize(token)
