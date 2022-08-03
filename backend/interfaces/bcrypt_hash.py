from passlib.context import CryptContext

from backend.services import HashInterface

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class BcryptHash(HashInterface):

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def hash(password: str) -> str:
        return pwd_context.hash(password)
