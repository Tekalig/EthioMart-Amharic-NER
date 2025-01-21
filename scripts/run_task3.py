from src.ner_training import load_conll_data, prepare_spacy_data, train_ner_model

# Define paths
data_path = "../data/labeled_data.conll"
train_data_path = "../data/train.spacy"
test_data_path = "../data/test.spacy"
output_model_dir = "../models/ner_model"

# Load, preprocess, and train the model
sentences, labels = load_conll_data(data_path)
prepare_spacy_data(sentences, labels, train_data_path)
train_ner_model(train_data_path, output_model_dir)

print("Task 3 completed: Model saved!")