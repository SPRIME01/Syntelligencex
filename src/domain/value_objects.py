from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class CaseStatus:
    status: str


@dataclass(frozen=True)
class ReourceType:
    type: str


@dataclass(frozen=True)
class CaseFileItemDefinition:
    name: str
    structure_ref: str


@dataclass(frozen=True)
class PlanItemDefinition:
    name: str
    type: str  # e.g., "HumanTask", "ProcessTask", "CaseTask", etc.


@dataclass(frozen=True)
class Sentry:
    name: str
    on_part: str
    if_part: Optional[str] = None
