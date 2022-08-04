from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import settings
from backend.app import user_router, todo_router


def register_db(app: FastAPI) -> FastAPI:
    register_tortoise(
        app,
        db_url=settings.TORTOISE_ORM["connections"]["default"],
        modules={"models": ["backend.interfaces.repository.tortoise.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    return app


def create_app() -> FastAPI:
    app = FastAPI(
        debug=bool(settings.DEBUG)
    )
    app.include_router(user_router)
    app.include_router(todo_router)
    app = register_db(app)
    return app


app = create_app()
