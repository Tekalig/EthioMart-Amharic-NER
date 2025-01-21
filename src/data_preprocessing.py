import re
from transformers import BertTokenizer

# Load the tokenizer for Amharic (example: XLM-Roberta or BERT)
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')


# Preprocess Amharic text (normalize, tokenize, remove unwanted characters)
def normalize_text(text):
    # Remove unnecessary symbols, punctuation, etc.
    text = re.sub(r'[^\w\s]', '', text)
    # Normalize spaces and newlines
    text = ' '.join(text.split())
    return text


def tokenize_text(text):
    # Tokenize using the tokenizer
    tokens = tokenizer.tokenize(text)
    return tokens


def preprocess_data(messages):
    preprocessed_messages = []

    for message in messages:
        content = message['content']
        if content:
            normalized_content = normalize_text(content)
            tokens = tokenize_text(normalized_content)
            message['tokens'] = tokens
            preprocessed_messages.append(message)

    return preprocessed_messages
