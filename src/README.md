# EthioMart-Amharic-NER SRC Folder

This folder contains the source code for the EthioMart-Amharic-NER project. The codebase is organized into modules and packages to facilitate modularity, reusability, and maintainability.

## Folder Structure

- `data_ingestion.py`: Module for data ingestion and preprocessing functions.
- `data_preprocessing.py`: Module for data preprocessing functions.
- `data_storage.py`: Module for data storage and retrieval functions.
- `data_labeling.py`: Module for data labeling functions.
- `ner_training.py`: Module for Named Entity Recognition (NER) model training functions.
- `ner_evaluation.py`: Module for NER model evaluation functions.
- `fastapi_server.py`: Module for FastAPI server implementation.
- `model_evaluation.py`: Module for model evaluation functions.
- `utils.py`: Module for utility functions used across the project.

## Key Features

1. **Modular Design**:
   - The codebase is organized into modules based on functionality, promoting code reuse and maintainability.
   - Each module focuses on a specific aspect of the project, such as data processing, model training, or evaluation.

2. **Reusability**:
   - Functions and classes are designed to be reusable across different parts of the project.
   - This reusability reduces redundancy and ensures consistency in the implementation.

3. **Scalability**:
   - The codebase is designed to scale with the project's requirements, allowing for easy integration of new features or enhancements.
   - New modules or functions can be added to accommodate additional tasks or functionalities.

4. **FastAPI Integration**:
    - The `fastapi_server.py` module provides an implementation of a FastAPI server for serving the NER model via API endpoints.
    - This integration enables easy deployment and consumption of the NER model as a web service.
5. **Logging**:
   - The codebase includes logging mechanisms to track execution and debug issues efficiently.
   - Logs are generated at different levels to provide detailed information about the workflow.

## Usage

1. Ensure the project dependencies are installed:
   ```bash
   pip install -r requirements.txt
    ```
2. Import the necessary modules and functions in your scripts or notebooks:
3. Use the functions provided in the modules for data processing, model training, evaluation, or server implementation.
4. Customize the functions or modules as needed to suit your specific requirements.
5. Run the scripts or notebooks to execute the desired tasks.
