from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from typing import Any


@dataclass(frozen=True)
class CreateCase:
    case_id: UUID
    project_id: str
    name: str
    description: str
    status: str
    assigned_to: str


@dataclass(frozen=True)
class UpdateCase:
    case_id: UUID
    title: str
    description: str
    status: str
    assigned_to: str


@dataclass(frozen=True)
class AddResource:
    case_id: UUID
    resource_type: str
    resource_id: str
    resource_name: str
    content: str


@dataclass(frozen=True)
class AssignCaseWorker:
    case_id: UUID
    worker_id: UUID
    role: str
    email: Optional[str] = None


@dataclass(frozen=True)
class ActivateStage:
    case_id: UUID
    stage_id: UUID


@dataclass(frozen=True)
class ChangePlanItemState:
    case_id: UUID
    plan_item_id: UUID
    new_state: str


@dataclass(frozen=True)
class UpdateCaseFileItem:
    case_id: UUID
    case_file_item_id: UUID
    new_value: Any