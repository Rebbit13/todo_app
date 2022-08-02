from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    uuid: UUID
