# scripts/run_task1.py
import sys
import os

# Add the src folder to the Python path so the modules can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.data_ingestion import fetch_messages
from src.data_preprocessing import preprocess_data
from src.data_storage import save_to_json, save_to_csv

def main():
    # Step 1: Ingest data
    print("Fetching messages from Telegram...")
    messages = fetch_messages()

    # Step 2: Preprocess data
    print("Preprocessing data...")
    preprocessed_data = preprocess_data(messages)

    # Step 3: Save the preprocessed data
    print("Saving data to JSON and CSV...")
    save_to_json(preprocessed_data)
    save_to_csv(preprocessed_data)

    print("Task 1 completed successfully!")

if __name__ == "__main__":
    main()
