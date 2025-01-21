from src.data_labeling import load_raw_data, label_data, save_labeled_data
from src.utils import clean_text

# Load the raw data (adjust the file path)
data = load_raw_data('../data/raw_data.csv')

# Clean the data (optional, if you want to clean text before labeling)
data['Message'] = data['Message'].apply(clean_text)

# Label the data
labeled_data = label_data(data)

# Save the labeled data in CoNLL format
save_labeled_data(labeled_data, '../data/labeled_data.conll')

print("Task 2: Data labeling completed and saved in CoNLL format.")
