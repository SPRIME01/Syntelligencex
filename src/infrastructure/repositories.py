# src/infrastructure/repositories.py

from uuid import UUID

from src.domain.entities import ModelDefinition, Project

from src.application.interfaces import ModelRepository, ProjectRepository


class InMemoryModelRepository(ModelRepository):

    """
    An in-memory repository for storing ModelDefinition entities.

    This implementation is suitable for development and testing purposes
    where persistence is not required. For production environments, consider
    using a database-backed repository.
    """

    def __init__(self):

        # Use a dictionary to store models in memory

        self.models: dict[UUID, ModelDefinition] = {}

    async def get_by_id(self, id: UUID) -> ModelDefinition:

        """Retrieve a ModelDefinition by its ID."""

        model = self.models.get(id)

        if not model:

            raise ValueError(f"Model with ID {id} not found")

        return model

    async def add(self, model: ModelDefinition) -> None:

        """Add a new ModelDefinition to the repository."""

        if model.id in self.models:

            raise ValueError(f"Model with ID {model.id} already exists")

        self.models[model.id] = model

    async def update(self, model: ModelDefinition) -> None:

        """Update an existing ModelDefinition in the repository."""

        if model.id not in self.models:

            raise ValueError(f"Model with ID {model.id} not found")

        self.models[model.id] = model

    async def delete(self, id: UUID) -> None:

        """Delete a ModelDefinition from the repository."""

        if id not in self.models:

            raise ValueError(f"Model with ID {id} not found")

        del self.models[id]


class InMemoryProjectRepository(ProjectRepository):
    """
    An in-memory repository for storing Project entities.
    Like InMemoryModelRepository, this is for development and testing and
    not suitable for production environments where data persistence is crucial.
    """

    def __init__(self):
        # Use a dictionary to store projects in memory
        self.projects: dict[UUID, Project] = {}

    async def get_by_id(self, id: UUID) -> Project:

        """Retrieve a Project by its ID."""

        project = self.projects.get(id)

        if not project:

            raise ValueError(f"Project with ID {id} not found")

        return project

    async def add(self, project: Project) -> None:

        """Add a new Project to the repository."""

        if project.id in self.projects:

            raise ValueError(f"Project with ID {project.id} already exists")

        self.projects[project.id] = project

    async def update(self, project: Project) -> None:

        """Update an existing Project in the repository."""

        if project.id not in self.projects:
            raise ValueError(f"Project with ID {project.id} not found")
        self.projects[project.id] = project

    async def delete(self, id: UUID) -> None:

        """Delete a Project from the repository."""

        if id not in self.projects:

            raise ValueError(f"Project with ID {id} not found")

        del self.projects[id]