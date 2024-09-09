# src/interfaces/api.py

from fastapi import FastAPI, Depends, HTTPException

from uuid import UUID

from typing import Dict, Any, List, Union

from src.application.services import ModelService, ProjectService

from src.infrastructure.repositories import InMemoryModelRepository, InMemoryProjectRepository

from src.domain.entities import ModelType, Project, ConceptualArtifact

from pydantic import BaseModel



# Create the FastAPI application instance

app = FastAPI()



# Dependency injection for services

def get_model_service():

    return ModelService(InMemoryModelRepository())



def get_project_service():

    return ProjectService(InMemoryProjectRepository())



# Pydantic model for creating a new model

class ModelCreateRequest(BaseModel):

    name: str

    model_type: ModelType



# Pydantic model for adding a field to a model

class FieldAddRequest(BaseModel):

    name: str

    field_type: str

    properties: Dict[str, Any]



# Pydantic model for creating a new project

class ProjectCreateRequest(BaseModel):

    name: str

    description: str



# Pydantic model for creating a new artifact

class ArtifactCreateRequest(BaseModel):

    name: str

    description: str

    content: Any

    artifact_type: str



# API endpoint for creating a new model

@app.post("/models", response_model=Dict[str, Union[str, UUID]])

async def create_model(

    model_request: ModelCreateRequest, service: ModelService = Depends(get_model_service)

) -> dict[str, Union[str, UUID]]:

    try:

        model_id = await service.create_model(model_request.name, model_request.model_type)

        return {"id": str(model_id)}

    except TypeError as e:

        raise HTTPException(

            status_code=400, detail=f"Error creating model: Invalid type - {str(e)}"

        )

    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



# API endpoint for adding a field to a model

@app.post("/models/{model_id}/fields", response_model=Dict[str, Union[str, UUID]])

async def add_field(

    model_id: UUID,

    field_request: FieldAddRequest,

    service: ModelService = Depends(get_model_service),

) -> dict[str, Union[str, UUID]]:

    try:

        field_id = await service.add_field(

            model_id,

            field_request.name,

            field_request.field_type,

            field_request.properties,

        )

        return {"id": str(field_id)}

    except TypeError as e:

        raise HTTPException(

            status_code=400, detail=f"Error adding field: Invalid type - {str(e)}"

        )

    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



# API endpoint for creating a new project

@app.post("/projects", response_model=Dict[str, Union[str, UUID]])

async def create_project(

    project_request: ProjectCreateRequest,

    service: ProjectService = Depends(get_project_service),

) -> dict[str, Union[str, UUID]]:

    try:

        project_id = await service.create_project(

            project_request.name, project_request.description

        )

        return {"id": str(project_id)}

    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



# API endpoint for adding a model to a project

@app.post("/projects/{project_id}/models", response_model=Dict[str, str])

async def add_model_to_project(

    project_id: UUID,

    model_id: UUID,

    service: ProjectService = Depends(get_project_service),

) -> dict[str, str]:

    try:

        await service.add_model_to_project(project_id, model_id)

        return {"message": "Model added to project successfully"}

    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



# API endpoint for creating a new artifact in a project

@app.post("/projects/{project_id}/artifacts", response_model=Dict[str, Union[str, UUID]])

async def create_artifact_in_project(

    project_id: UUID,

    artifact_request: ArtifactCreateRequest,

    service: ProjectService = Depends(get_project_service),

) -> dict[str, Union[str, UUID]]:

    try:

        artifact_id = await service.create_artifact_in_project(

            project_id,

            artifact_request.name,

            artifact_request.description,

            artifact_request.content,

            artifact_request.artifact_type,

        )

        return {"id": str(artifact_id)}

    except ValueError as e:

        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



# API endpoint for listing all projects

@app.get("/projects", response_model=List[Project])

async def list_projects(service: ProjectService = Depends(get_project_service)):

    # In a production setting, you'd likely paginate this

    return await service.list_projects()





# API endpoint for retrieving a specific project by ID

@app.get("/projects/{project_id}", response_model=Project)

async def get_project(project_id: UUID, service: ProjectService = Depends(get_project_service)):

    try:

        return await service.get_project(project_id)

    except ValueError as e:

        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")



# API endpoint for listing all conceptual artifacts within a project

@app.get("/projects/{project_id}/artifacts", response_model=List[ConceptualArtifact])

async def list_artifacts_in_project(

    project_id: UUID, service: ProjectService = Depends(get_project_service)

):

    try:

        return await service.list_artifacts_in_project(project_id)

    except ValueError as e:

        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")