from datetime import datetime, timedelta
from uuid import UUID

import jwt
from jwt import InvalidSignatureError, DecodeError

from settings import JWT_SECRET, JWT_ALGORITHM, JWT_PAYLOAD_TIME_FORMAT
from .exceptions import TokenBroken, TokenExpired
from backend.services import TokenInterface, TokenPayload, NotAuthorized, TokenType


class JWTTokenService(TokenInterface):
    secret: str = JWT_SECRET
    algorithm: str = JWT_ALGORITHM
    time_format: str = JWT_PAYLOAD_TIME_FORMAT

    def decode_access_token(self, token: str) -> TokenPayload:
        try:
            decoded_token = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except InvalidSignatureError:
            raise NotAuthorized("Not authorized")
        except DecodeError:
            raise TokenBroken("Token is invalid")
        expired_at = datetime.strptime(decoded_token['exceed'], self.time_format)
        if expired_at < datetime.utcnow():
            raise TokenExpired("Token expired")
        return TokenPayload(**decoded_token)

    def create_token(
        self,
        user_uuid: UUID,
        token_type: TokenType,
        living_time: timedelta,
    ) -> str:
        payload = TokenPayload(
            user_uuid=user_uuid,
            token_type=token_type,
            exceed=datetime.strftime(datetime.utcnow() + living_time, self.time_format),
        )
        return jwt.encode(payload.__dict__, self.secret, algorithms=self.algorithm)
