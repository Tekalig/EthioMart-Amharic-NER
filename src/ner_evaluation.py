import spacy
from sklearn.metrics import classification_report
from spacy.training import offsets_to_biluo_tags

# Function to load the trained model
def load_trained_model(model_path):
    """Load the trained spaCy NER model."""
    return spacy.load(model_path)

# Function to parse CoNLL test data
def parse_conll_data(file_path):
    """Parse test data in CoNLL format."""
    sentences = []
    true_labels = []

    with open(file_path, "r", encoding="utf-8") as file:
        sentence = []
        labels = []

        for line in file:
            line = line.strip()
            if line == "":
                if sentence:
                    sentences.append(" ".join(sentence))
                    true_labels.append(labels)
                    sentence = []
                    labels = []
            else:
                token, label = line.split()
                sentence.append(token)
                labels.append(label)

    return sentences, true_labels

# Function to evaluate the model
def evaluate_model(model, sentences, true_labels):
    """Evaluate the model on test data."""
    predicted_labels = []

    for sentence in sentences:
        doc = model(sentence)
        biluo_tags = offsets_to_biluo_tags(doc, [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents])
        predicted_labels.append(biluo_tags)

    # Flatten the true and predicted labels for comparison
    flat_true_labels = [label for seq in true_labels for label in seq]
    flat_predicted_labels = [label for seq in predicted_labels for label in seq]

    # Generate a classification report
    report = classification_report(flat_true_labels, flat_predicted_labels, zero_division=0)
    print("Model Evaluation Report:")
    print(report)

# Function to interpret model predictions
def interpret_model_with_shap(model, sentences):
    """Interpret model predictions using SHAP (transformer-based models)."""
    try:
        import shap
    except ImportError:
        print("SHAP library is not installed. Please install it using `pip install shap`.")
        return

    explainer = shap.Explainer(model)
    shap_values = explainer(sentences)

    # Visualize the explanations
    shap.plots.text(shap_values[0])

# Main function to orchestrate evaluation and interpretation
def main(model_path, test_data_path):
    """Main function to evaluate and interpret the NER model."""
    model = load_trained_model(model_path)
    sentences, true_labels = parse_conll_data(test_data_path)

    # Evaluate the model
    evaluate_model(model, sentences, true_labels)

    # Interpret the model predictions
    sample_sentence = sentences[0]
    print(f"Interpreting model predictions for the sample sentence: {sample_sentence}")
    interpret_model_with_shap(model, [sample_sentence])

