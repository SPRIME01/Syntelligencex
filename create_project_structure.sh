#!/bin/zsh

# Create directories
mkdir -p src/domain/artifacts
mkdir -p src/application
mkdir -p src/infrastructure/databases
mkdir -p src/infrastructure/ai
mkdir -p src/infrastructure/blockchain
mkdir -p src/infrastructure/communication
mkdir -p src/infrastructure/runtime
mkdir -p src/interfaces
mkdir -p src/sdk/visual_modeler
mkdir -p tests/unit
mkdir -p tests/integration

# Create files
touch src/domain/__init__.py
touch src/domain/entities.py
touch src/domain/events.py
touch src/domain/artifacts/__init__.py
touch src/domain/artifacts/entities.py
touch src/domain/artifacts/events.py

touch src/application/__init__.py
touch src/application/interfaces.py
touch src/application/services.py

touch src/infrastructure/__init__.py
touch src/infrastructure/repositories.py
touch src/infrastructure/databases/__init__.py
touch src/infrastructure/databases/vespa_client.py
touch src/infrastructure/databases/arango_client.py
touch src/infrastructure/databases/deeplake_client.py

touch src/infrastructure/ai/__init__.py
touch src/infrastructure/ai/llama_index_client.py
touch src/infrastructure/ai/lang_graph_client.py
touch src/infrastructure/ai/lang_chain_client.py
touch src/infrastructure/ai/qiskit_client.py
touch src/infrastructure/ai/tensorflow_federated_client.py
touch src/infrastructure/ai/shap_client.py
touch src/infrastructure/ai/openai_gym_client.py
touch src/infrastructure/ai/h2o_client.py

touch src/infrastructure/blockchain/__init__.py
touch src/infrastructure/blockchain/hyperledger_fabric_client.py

touch src/infrastructure/communication/__init__.py
touch src/infrastructure/communication/grpc_server.py
touch src/infrastructure/communication/kafka_client.py

touch src/infrastructure/runtime/__init__.py
touch src/infrastructure/runtime/wasm_runtime.py

touch src/interfaces/__init__.py
touch src/interfaces/api.py

touch src/sdk/__init__.py
touch src/sdk/dsl.py
touch src/sdk/generators.py
touch src/sdk/visual_modeler/__init__.py

touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py

touch .gitignore
touch main.py

echo "Project structure created successfully!"
