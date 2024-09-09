from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import List, Dict, Any, Optional, Union, Set
from enum import Enum
from datetime import datetime
from src.domain.artifacts.value_objects import CustomInstruction
from src.domain.value_objects import PlanItemDefinition, Sentry, CaseFileItemDefinition


class ModelType(Enum):
    ENTITY = "entity"
    VALUE_OBJECT = "value_object"
    AGGREGATE = "aggregate"


@dataclass
class FieldDefinition:
    id: UUID = field(default_factory=uuid4)
    name: str
    type: str
    properties: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("Field name must be a string")
        if not self.name:
            raise ValueError("Field name cannot be empty")
        if not isinstance(self.type, str):
            raise TypeError("Field type must be a string")
        if not self.type:
            raise ValueError("Field type cannot be empty")


@dataclass
class ModelDefinition:
    id: UUID = field(default_factory=uuid4)
    name: str
    type: ModelType
    fields: List[FieldDefinition] = field(default_factory=list)
    # Add the missing ARP concepts here
    nodes: List['Node'] = field(default_factory=list)
    items: List['Item'] = field(default_factory=list)
    movements: List['Movement'] = field(default_factory=list)
    paths: List['Path'] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("Model name must be a string")
        if not self.name:
            raise ValueError("Model name cannot be empty")
        if not isinstance(self.type, ModelType):
            raise TypeError("Model type must be a ModelType enum")

    def add_field(self, field: FieldDefinition):
        if not isinstance(field, FieldDefinition):
            raise TypeError("Field must be a FieldDefinition instance")
        if any(f.name == field.name for f in self.fields):
            raise ValueError(f"Field with name '{field.name}' already exists")
        self.fields.append(field)

    def remove_field(self, field_name: str):
        self.fields = [f for f in self.fields if f.name != field_name]


@dataclass
class NodeType(Enum):
    HUMAN_AGENT = "human_agent"
    AI_AGENT = "ai_agent"
    API_ENDPOINT = "api_endpoint"
    ORGANIZATION = "organization"


@dataclass
class Node:
    id: UUID = field(default_factory=uuid4)
    name: str
    node_type: NodeType 
    # Add other relevant attributes for Node


@dataclass
class Item:
    id: UUID = field(default_factory=uuid4)
    # Add other relevant attributes for Item


@dataclass
class Movement:
    id: UUID = field(default_factory=uuid4)
    # Add other relevant attributes for Movement


@dataclass
class Path:
    id: UUID = field(default_factory=uuid4)
    # Add other relevant attributes for Path


@dataclass
class ConceptualArtifact:
    id: UUID = field(default_factory=uuid4)
    name: str
    description: str
    content: Any  # This could store code, data, rules, etc. 
    artifact_type: str
    # Add a field to potentially link to a generated agent 
    agent_instance: Union['Agent', None] = field(default=None) 


@dataclass
class Agent:  # You might want to explore different agent architectures
    id: UUID = field(default_factory=uuid4)
    name: str
    artifact_source: ConceptualArtifact
    # ... (Add fields for agent capabilities, state, etc.)


@dataclass
class Project:
    id: UUID = field(default_factory=uuid4)
    name: str
    description: str
    models: List[ModelDefinition] = field(default_factory=list)
    artifacts: List[ConceptualArtifact] = field(default_factory=list)
    knowledge_base: Dict[str, Any] = field(default_factory=dict)
    case: Optional[List[Case]] = field(default=None)
    status: str
    created_date: datetime = field(default_factory=datetime.now)
    updated_date: datetime = field(default_factory=datetime.now)
    custom_instructions: Set[CustomInstruction] = field(default_factory=frozenset)


@dataclass
class Case:
    id: UUID = field(default_factory=uuid4)
    title: str
    description: str
    assigned_to: str
    resources: Dict[str, Resource] = field(default_factory=dict)
    project: Project
    status: str
    created_date: str
    updated_date: str
    knowledge_base: Dict[str, Any] = field(default_factory=dict)
    events: List[Any] = field(default_factory=list)


@dataclass
class CaseWorker:
    id: UUID = field(default_factory=uuid4)
    name: str
    role: str
    email: Optional[str] = None
    relationships: Dict[str, Case] = field(default_factory=dict)


@dataclass
class User:
    id: UUID = field(default_factory=uuid4)
    username: str
    projects: List[Project] = field(default_factory=list)
    email: str


@dataclass
class CaseFileItem:
    id: UUID = field(default_factory=uuid4)
    definition: CaseFileItemDefinition
    value: Any


@dataclass
class PlanItem:
    id: UUID = field(default_factory=uuid4)
    definition: PlanItemDefinition
    state: str = "Available"
    entry_criteria: List[Sentry] = field(default_factory=list)
    exit_criteria: List[Sentry] = field(default_factory=list)


@dataclass
class Stage:
    id: UUID = field(default_factory=uuid4)
    name: str
    plan_items: List[PlanItem] = field(default_factory=list)
    entry_criteria: List[Sentry] = field(default_factory=list)
    exit_criteria: List[Sentry] = field(default_factory=list)


@dataclass
class Case:
    id: UUID = field(default_factory=uuid4)
    name: str
    stages: List[Stage] = field(default_factory=list)
    case_file_items: List[CaseFileItem] = field(default_factory=list)
