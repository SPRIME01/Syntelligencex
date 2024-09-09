from dataclasses import dataclass
from uuid import UUID
from src.domain.artifacts.value_objects import ContentType, Version


@dataclass
class ArtifactCreated:
    artifact_id: UUID
    content: str
    content_type: ContentType


@dataclass
class ArtifactUpdated:
    artifact_id: UUID
    new_content: str
    new_version: Version


@dataclass
class ArtifactAddedToProject:
    artifact_id: UUID
    project_id: UUID