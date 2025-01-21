# EthioMart-Amharic-NER Scripts Folder

This folder contains executable scripts designed to perform specific tasks in the project. These scripts act as the main entry points for running workflows, leveraging modularized code from the `src` folder for efficiency and reusability.

## Folder Structure

- `main.py`: Script for Task 1 - Exploratory Data Analysis (EDA) on customer purchasing behavior.
- `run_task2.py`: Script for Task 2 - User Engagement Analysis.
- `run_task3.py`: Script for Task 3 - Experience Analytics.
- `model_evaluation.py`: Script for Task 4 - Satisfaction Analysis.

## Key Features

1. **Task-Specific Execution**:
   - Each script corresponds to a distinct task and provides a simple way to execute its workflow.

2. **Integration with `src` Folder**:
   - Scripts import reusable functions and modules from the `src` folder to ensure modularity and maintainability.

3. **Environment Configuration**:
   - Scripts load configuration settings from a `.env` file, ensuring secure and flexible parameter management.

4. **Logging**:
   - All scripts include logging mechanisms to track execution and debug issues efficiently.

5. **Ease of Use**:
   - Scripts are designed for standalone execution, making them user-friendly for both manual and automated workflows.

## Usage

1. Ensure the project dependencies are installed:
   ```bash
   pip install -r requirements.txt
    ```
2. Prepare the .env file with necessary environment variables.

3. Run the desired script:
```bash
    python main.py
```
```bash
    python run_task2.py
```
```bash
    python run_task3.py
```
```bash
    python model_evaluation.py
```
