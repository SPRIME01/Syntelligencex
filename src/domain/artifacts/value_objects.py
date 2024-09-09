from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass(frozen=True)
class ContentType(Enum):
    TEXT = "text"
    CODE = "code"
    WEBPAGE = "webpage"
    DIAGRAM = "diagram"


@dataclass(frozen=True)
class Version:
    number: int
    timestamp: datetime
    changes: str


@dataclass(frozen=True)
class CustomInstruction:
    instruction: str
    priority: int