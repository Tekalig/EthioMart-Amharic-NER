# EthioMart: Telegram E-Commerce Centralization with Amharic NER

## Overview
EthioMart aims to centralize e-commerce activities on Telegram by consolidating data from multiple Ethiopian-based Telegram channels into one unified platform. This project focuses on fine-tuning large language models (LLMs) for Amharic Named Entity Recognition (NER) to extract key business entities like product names, prices, and locations from text, images, and documents shared across Telegram channels.

## Business Need
Telegram is increasingly popular for business transactions in Ethiopia, but its decentralized nature makes it difficult for vendors and customers to navigate multiple channels. EthioMart solves this problem by creating a centralized platform that aggregates and processes real-time data, enabling users to explore and interact with multiple vendors in one place.

## Key Objectives
- Real-time data extraction from Telegram channels.
- Fine-tuning LLMs to extract entities such as product names, prices, and locations.
- Creating a comprehensive e-commerce hub for Ethiopian businesses.

## Possible Entities
- **Product Names or Types**
- **Material or Ingredients**
- **Location Mentions**
- **Monetary Values or Prices**

## Data
- **Source**: Messages and data from Ethiopian-based Telegram e-commerce channels.
- **Types**:
  - Text (Amharic language messages)
  - Images (Product images, marketing materials)

### Example Channels
- ShagerOnlineStore
- AddisMart
- EthiopiaDeals
- BoleMarket
- AbayOnline

## Project Structure
```plaintext
EthioMart-Amharic-NER/
├── data/                # Raw and preprocessed data
├── src/                 # Source code
│   ├── data_ingestion.py   # Scraper for Telegram channels
│   ├── preprocessing.py    # Data preprocessing functions
│   ├── fine_tune_ner.py    # Code for fine-tuning NER models
│   ├── model_comparison.py # Model evaluation and comparison
│   ├── interpretability.py # Model interpretability tools
├── notebooks/           # Jupyter notebooks for EDA and experimentation
├── models/              # Saved fine-tuned models
├── results/             # Evaluation metrics and reports
├── scripts/             # Main scripts
│   ├── main.py          # Main script to run the project
├── README.md            # Project documentation
└── requirements.txt     # Dependencies
```
## Tasks

### Task 1: Data Ingestion and Preprocessing
- **Goal**: Set up a system to fetch and preprocess data from Telegram channels.
- **Steps**:
  1. Identify and connect to relevant Telegram channels using a custom scraper.
  2. Implement a message ingestion system to collect text, images, and documents in real time.
  3. Preprocess text data by tokenizing, normalizing, and handling Amharic-specific linguistic features.
  4. Clean and structure the data into a unified format, separating metadata from message content.
  5. Store preprocessed data in a structured format (e.g., JSON or CSV).

### Task 2: Label a Subset of Dataset in CoNLL Format
- **Goal**: Label entities such as products, prices, and locations in the dataset.
- **Format**: CoNLL (one token per line with entity labels).
- **Deliverable**: A labeled dataset in plain text format.

### Task 3: Fine-Tune NER Model
- **Goal**: Fine-tune pre-trained LLMs like XLM-Roberta or AfroXMLR for Amharic NER tasks.
- **Steps**:
  1. Load the labeled dataset from Task 2.
  2. Tokenize the data and align labels with tokens.
  3. Fine-tune using Hugging Face's Trainer API.
  4. Save the fine-tuned model.

### Task 4: Model Comparison and Selection
- **Goal**: Compare models like XLM-Roberta, DistilBERT, and mBERT.
- **Steps**:
  1. Fine-tune multiple models.
  2. Evaluate performance using metrics like F1-score, precision, and recall.
  3. Select the best-performing model for production.

### Task 5: Model Interpretability
- **Goal**: Ensure transparency by interpreting model predictions.
- **Steps**:
  1. Use SHAP and LIME to analyze model predictions.
  2. Identify and document areas for improvement.

## Dependencies
- Python 3.8+
- Libraries:
  - Telethon
  - pandas
  - numpy
  - transformers (Hugging Face)
  - SHAP
  - LIME
  - scikit-learn
  - matplotlib
  - seaborn
 

## How to Run
Clone the repository:
```bash
  git clone https://github.com/Tekalig/EthioMart-Amharic-NER.git
  ```

Navigate to the project directory:
```bash
  cd EthioMart-Amharic-NER 
  ```
Set up the environment and install dependencies:
```bash
  pip install -r requirements.txt
  ```
Set up Telegram API credentials for data ingestion.
Run the main script:
```bash
  python scripts/main.py
  ```
  
Alternatively, you can explore the Jupyter notebooks for experimentation:
jupyter notebook notebooks/

Contribution
Contributions are welcome! Please fork the repository and create a pull request for review.  

License
This project is licensed under the GNU License.