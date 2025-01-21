import json
import pandas as pd

# Save preprocessed data to JSON
def save_to_json(data, filename="preprocessed_data.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Save preprocessed data to CSV
def save_to_csv(data, filename="preprocessed_data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
