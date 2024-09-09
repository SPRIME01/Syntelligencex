from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Set, Optional, Union
from uuid import UUID, uuid4
from src.domain.artifacts.value_objects import ContentType, Version


@dataclass
class ConceptualArtifact:
    id: UUID = field(default_factory=uuid4)
    content: str
    content_type: ContentType
    versions: List[Version] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    ageent_instance: Optional[Union['Agent', None]] = field(default=None)


@dataclass
class KnowledgeBaseItem:
    id: UUID = field(default_factory=uuid4)
    content: str
    content_type: ContentType
    tags: Set[str] = field(default_factory=frozenset)