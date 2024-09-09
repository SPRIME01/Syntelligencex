from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import Dict, Any


@dataclass(frozen=True)
class CaseEvent:
    id: UUID = field(default_factory=uuid4)
    event_type: str
    timestamp: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class CaseCreated:
    case_id: UUID
    name: str


@dataclass(frozen=True)
class StageActivated:
    case_id: UUID
    stage_id: UUID


@dataclass(frozen=True)
class PlanItemStateChanged:
    case_id: UUID
    plan_item_id: UUID
    new_state: str


@dataclass(frozen=True)
class CaseFileItemChanged:
    case_id: UUID
    case_file_item_id: UUID
    new_value: Any


@dataclass(frozen=True)
class CaseUpdated(CaseEvent):
    case_id: UUID


@dataclass(frozen=True)
class CaseClosed(CaseEvent):
    case_id: UUID


@dataclass(frozen=True)
class CaseReopened(CaseEvent):
    case_id: UUID


@dataclass(frozen=True)
class CaseAssigned(CaseEvent):
    case_id: UUID
    worker_id: UUID


@dataclass(frozen=True) 
class ResourceAdded(CaseEvent):
    case_id: UUID
