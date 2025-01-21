import pandas as pd


# Function to load raw data (e.g., from CSV or JSON)
def load_raw_data(file_path):
    data = pd.read_csv(file_path)  # Change to your specific file type if needed
    return data


# Function to label the data in CoNLL format
def label_data(data):
    labeled_data = []

    # Loop through each message in the data
    for message in data['Message']:  # Adjust the column name if necessary
        tokens = message.split()  # Tokenizing by space; adjust if more advanced tokenization is needed
        labeled_message = []

        # Example logic for labeling; this should be updated with actual labeling logic
        for token in tokens:
            # Simple example for labeling entities; you need to implement real labeling rules
            if token.lower() in ['addis', 'abeba']:  # Example for location
                labeled_message.append((token, 'B-LOC'))
            elif token.isdigit():  # Example for price
                labeled_message.append((token, 'B-PRICE'))
            else:  # For product or non-entity tokens
                labeled_message.append((token, 'O'))

        labeled_data.append(labeled_message)

    return labeled_data


# Function to save the labeled data in CoNLL format
def save_labeled_data(labeled_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for message in labeled_data:
            for token, label in message:
                file.write(f"{token} {label}\n")
            file.write("\n")  # Blank line between sentences/messages
