import re

# Function to clean Amharic text (basic cleaning, extend as needed)
def clean_text(text):
    # Remove unwanted characters (e.g., punctuation, extra spaces)
    cleaned_text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    cleaned_text = re.sub(r'[^\w\sአ-፲]', '', cleaned_text)  # Remove non-Amharic characters
    return cleaned_text
