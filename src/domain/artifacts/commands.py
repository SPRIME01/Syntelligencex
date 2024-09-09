from dataclasses import dataclass
from uuid import UUID
from src.domain.artifacts.value_objects import ContentType


@dataclass
class CreateArtifact:
    content: str
    content_type: ContentType


@dataclass
class UpdateArtifact:
    artifact_id: UUID
    new_content: str


@dataclass
class AddArtifactToProject:
    artifact_id: UUID
    project_id: UUID