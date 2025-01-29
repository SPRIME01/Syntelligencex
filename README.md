# Syntelligence

## Project description

Syntelligence is a project that provides a framework for managing and analyzing cases, artifacts, and agents. It includes various services and interfaces to handle different aspects of case management, artifact creation, and agent management.

## Features

* Case management: Create, update, and manage cases and their associated resources.
* Artifact management: Generate, render, and manage artifacts based on user prompts and content types.
* Agent management: Create and manage AI agents from conceptual artifacts.
* Visualization: Generate and update CMMN diagrams based on case changes.
* Analysis: Analyze case progression and generate case statistics.
* Integration: Integrate with external services and publish events.

## Project structure

The project is organized into several directories and files:

* `src/application`: Contains the application layer with services and interfaces for managing cases, artifacts, and agents.
  * `src/application/services/agent_management_service.py`
  * `src/application/services/artifact_services.py`
  * `src/application/services/case_analysis_service.py`
  * `src/application/services/case_event_service.py`
  * `src/application/services/case_file_service.py`
  * `src/application/services/case_managment_service.py`
  * `src/application/services/case_visualization_service.py`
  * `src/application/services/plan_item_service.py`
  * `src/application/services/sentry_service.py`
* `src/domain`: Contains the domain layer with entities, aggregates, commands, events, and ports.
  * `src/domain/aggregates.py`
  * `src/domain/commands.py`
  * `src/domain/entities.py`
  * `src/domain/events.py`
  * `src/domain/ports.py`
* `src/infrastructure`: Contains the infrastructure layer with implementations for repositories, AI clients, blockchain clients, communication clients, and databases.
  * `src/infrastructure/repositories.py`
* `src/interfaces`: Contains the interfaces layer with API endpoints for interacting with the application.
  * `src/interfaces/api.py`
* `src/sdk`: Contains the SDK for interacting with the application programmatically.
* `tests`: Contains the test cases for the project.

## Installation

1. Clone the repository.
2. Install the required dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

1. Run the FastAPI application:
   ```bash
   poetry run uvicorn src.interfaces.api:app --reload
   ```
2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
