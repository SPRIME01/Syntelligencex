from domain.ports import AgentCreationPort

from domain.entities import Agent, ConceptualArtifact



class AgentService:

    def __init__(self, artifact_repository, agent_creator: AgentCreationPort):

        self.artifact_repository = artifact_repository

        self.agent_creator = agent_creator # Dependency Injection



    def create_agent_from_artifact(self, artifact_id: UUID) -> Agent:

        artifact = self.artifact_repository.get_by_id(artifact_id)

        agent = self.agent_creator.create_agent(artifact)

        artifact.agent_instance = agent

        self.artifact_repository.save(artifact)

        return agent