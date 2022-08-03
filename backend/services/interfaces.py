from abc import ABCMeta
from dataclasses import dataclass
from datetime import timedelta, datetime
from enum import Enum
from uuid import UUID


class HashInterface(metaclass=ABCMeta):

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        raise NotImplemented

    @staticmethod
    def hash(password: str) -> str:
        raise NotImplemented


class TokenType(Enum):
    access = "access"
    refresh = "refresh"


@dataclass
class TokenPayload:
    user_uuid: UUID
    token_type: TokenType
    exceed: str


class TokenInterface(metaclass=ABCMeta):

    @staticmethod
    def decode_access_token(token: str) -> TokenPayload:
        raise NotImplemented

    @staticmethod
    def create_token(
        user_uuid: UUID,
        token_type: TokenType,
        living_time: timedelta,
    ) -> str:
        raise NotImplemented
