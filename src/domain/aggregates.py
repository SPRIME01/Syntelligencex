from dataclasses import dataclass, field
from typing import Dict
from uuid import UUID
from src.domain.entities import Case, PlanItem, CaseFileItem


@dataclass
class CaseAggregate:
    case: Case
    plan_items: Dict[UUID, PlanItem] = field(default_factory=dict)
    case_file_items: Dict[UUID, CaseFileItem] = field(default_factory=dict)

    def add_plan_item(self, plan_item: PlanItem):
        self.plan_items[plan_item.id] = plan_item

    def add_case_file_item(self, case_file_item: CaseFileItem):
        self.case_file_items[case_file_item.id] = case_file_item