from dataclasses import dataclass
from uuid import UUID


@dataclass
class Owner:
    uuid: UUID | None = None
