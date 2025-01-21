from fastapi import FastAPI
import spacy
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Load the trained model
MODEL_PATH = "../models/ner_model"
nlp = spacy.load(MODEL_PATH)

# Input and output models for API
class TextInput(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    entities: List[Dict[str, str]]

@app.get("/")
def root():
    return {"message": "NER Model API is running!"}

@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: TextInput):
    """Perform NER on the input text."""
    doc = nlp(input_data.text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}
