from src.ner_evaluation import main

# Define paths
MODEL_PATH = "../models/ner_model"
TEST_DATA_PATH = "../data/test_data.conll"

# Evaluate and interpret the model
main(MODEL_PATH, TEST_DATA_PATH)
