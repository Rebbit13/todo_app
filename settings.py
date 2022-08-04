import os

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_PAYLOAD_TIME_FORMAT = os.getenv("JWT_PAYLOAD_TIME_FORMAT")

LOG_LEVEL = os.getenv("LOG_LEVEL")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    },
    "apps": {
        "models": {
            "models": ["backend.interfaces.repository.tortoise.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
