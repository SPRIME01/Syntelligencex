from abc import ABC, abstractmethod
from .entities import Agent, ConceptualArtifact
from typing import List, Dict, Any
from uuid import UUID


# Agent Creation Port
class AgentCreationPort(ABC):

    @abstractmethod
    def create_agent(self, artifact: ConceptualArtifact) -> Agent:

        """Creates an AI agent from a given ConceptualArtifact."""

        pass


# Case Management Port
class CaseManagementPort(ABC):
    @abstractmethod
    def create_case(self, name: str) -> UUID:
        pass

    @abstractmethod
    def get_case(self, case_id: UUID) -> Dict[str, Any]:
        pass

    @abstractmethod
    def update_case(self, case_id: UUID, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def delete_case(self, case_id: UUID) -> None:
        pass


# Stage Management Port
class StageManagementPort(ABC):
    @abstractmethod
    def activate_stage(self, case_id: UUID, stage_id: UUID) -> None:
        pass

    @abstractmethod
    def complete_stage(self, case_id: UUID, stage_id: UUID) -> None:
        pass

    @abstractmethod
    def get_stage_status(self, case_id: UUID, stage_id: UUID) -> str:
        pass


# Plan Item Management Port
class PlanItemManagementPort(ABC):
    @abstractmethod
    def create_plan_item(self, case_id: UUID, data: Dict[str, Any]) -> UUID:
        pass

    @abstractmethod
    def update_plan_item_state(self, case_id: UUID, plan_item_id: UUID, new_state: str) -> None:
        pass

    @abstractmethod
    def get_plan_item_details(self, case_id: UUID, plan_item_id: UUID) -> Dict[str, Any]:
        pass


# Case File Management Port
class CaseFileManagementPort(ABC):
    @abstractmethod
    def add_case_file_item(self, case_id: UUID, data: Dict[str, Any]) -> UUID:
        pass

    @abstractmethod
    def update_case_file_item(self, case_id: UUID, item_id: UUID, data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get_case_file_item(self, case_id: UUID, item_id: UUID) -> Dict[str, Any]:
        pass


# Sentry Evaluation Port
class SentryEvaluationPort(ABC):
    @abstractmethod
    def evaluate_sentry(self, case_id: UUID, sentry_id: UUID) -> bool:
        pass

    @abstractmethod
    def trigger_sentry_action(self, case_id: UUID, sentry_id: UUID) -> None:
        pass


# Case Visualization Port
class CaseVisualizationPort(ABC):
    @abstractmethod
    def generate_cmmn_diagram(self, case_id: UUID) -> bytes:
        pass

    @abstractmethod
    def update_diagram(self, case_id: UUID) -> bytes:
        pass


# Case Analysis Port
class CaseAnalysisPort(ABC):
    @abstractmethod
    def analyze_case_progression(self, case_id: UUID) -> Dict[str, Any]:
        pass

    @abstractmethod
    def generate_case_statistics(self, case_id: UUID) -> Dict[str, Any]:
        pass


# User Authentication Port
class UserAuthenticationPort(ABC):
    @abstractmethod
    def authenticate_user(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_user_permissions(self, user_id: UUID) -> List[str]:
        pass


# Persistence Port
class PersistencePort(ABC):
    @abstractmethod
    def save_entity(self, entity_type: str, data: Dict[str, Any]) -> UUID:
        pass

    @abstractmethod
    def retrieve_entity(self, entity_type: str, entity_id: UUID) -> Dict[str, Any]:
        pass

    @abstractmethod
    def delete_entity(self, entity_type: str, entity_id: UUID) -> None:
        pass


# Event Publishing Port
class EventPublishingPort(ABC):
    @abstractmethod
    def publish_event(self, event_type: str, event_data: Dict[str, Any]) -> None:
        pass


# External Service Integration Port
class ExternalServiceIntegrationPort(ABC):
    @abstractmethod
    def integrate_external_service(self, service_name: str, action: str, data: Dict[str, Any]) -> Any:
        pass
