from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .app_constructor import user_cases
from .oauth_scheme import oauth2_scheme

router = APIRouter(prefix="/user")


@router.post("/sign_up")
async def register(form: OAuth2PasswordRequestForm = Depends()):
    access_token, refresh_token = await user_cases.register(form.username, form.password)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post("/sign_in")
async def sign_in(form: OAuth2PasswordRequestForm = Depends()):
    access_token, refresh_token = await user_cases.sign_in(form.username, form.password)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post("/refresh")
async def refresh(token: str = Depends(oauth2_scheme)):
    access_token, refresh_token = await user_cases.refresh(token)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.patch("/change_password")
async def change_password(
        new_password: str,
        form: OAuth2PasswordRequestForm = Depends(),
):
    await user_cases.change_password(form.username, form.password, new_password)
    return {"message": "ok"}
