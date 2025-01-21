import os
import random
import spacy
from spacy.tokens import DocBin

# Function to load labeled data in CoNLL format
def load_conll_data(file_path):
    sentences = []
    labels = []

    with open(file_path, 'r', encoding='utf-8') as file:
        sentence = []
        entities = []

        for line in file:
            line = line.strip()
            if line == "":  # End of a sentence
                if sentence:
                    sentences.append(sentence)
                    labels.append(entities)
                    sentence = []
                    entities = []
            else:
                token, label = line.split()
                sentence.append(token)
                entities.append(label)

    return sentences, labels

# Function to convert data to spaCy's DocBin format
def prepare_spacy_data(sentences, labels, output_path):
    nlp = spacy.blank("xx")  # Use a blank multilingual model; replace "xx" with "am" if Amharic support is added
    doc_bin = DocBin()

    for sentence, label_sequence in zip(sentences, labels):
        doc = nlp.make_doc(" ".join(sentence))
        entities = []
        start = 0

        for token, label in zip(sentence, label_sequence):
            if label.startswith("B-"):
                entity_type = label[2:]
                start = doc.text.find(token, start)
                end = start + len(token)
                entities.append((start, end, entity_type))

        doc.ents = [spacy.tokens.Span(doc, doc.char_span(start, end)[0], doc.char_span(start, end)[1], label=label)
                    for start, end, label in entities]
        doc_bin.add(doc)

    doc_bin.to_disk(output_path)

# Function to train the NER model
def train_ner_model(train_data_path, output_model_dir, n_iter=10):
    nlp = spacy.blank("xx")  # Use a blank multilingual model

    # Add the NER pipeline
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)

    # Load training data
    doc_bin = DocBin().from_disk(train_data_path)
    docs = list(doc_bin.get_docs(nlp.vocab))

    # Add labels to the NER component
    for doc in docs:
        for ent in doc.ents:
            ner.add_label(ent.label_)

    # Train the model
    optimizer = nlp.begin_training()
    for i in range(n_iter):
        random.shuffle(docs)
        losses = {}
        for doc in docs:
            nlp.update([doc], losses=losses, drop=0.1)
        print(f"Iteration {i + 1}, Losses: {losses}")

    # Save the trained model
    nlp.to_disk(output_model_dir)
    print(f"Model saved to {output_model_dir}")
