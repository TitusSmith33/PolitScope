"""Experimental functions testing PolitScope."""

import torch
import itertools

from text_processor import preprocess_text
from embedding import generate_embeddings


BASE_LINE = {"content": "Donald Trump is a great president."}

subjects = ["Donald Trump", "Joe Biden", "Ron Cole", "The mayor", "Anakan Skywalker"]
adjectives = ["great", "honest", "corrupt", "terrible", "neutral"]
nouns = ["president", "leader", "golfer", "Jedi", "role model"]

def generate_sentences():
    sentences = [
        f"{subject} is a {adjective} {noun}."
        for subject, adjective, noun in itertools.product(subjects, adjectives, nouns)
    ]
    dataset = {"content": " ".join(sentences)}
    return dataset


def compute_distances(embedding1, embedding2):
    """Compute Euclidean distance between two embeddings."""
    tensor1 = torch.tensor(embedding1)
    tensor2 = torch.tensor(embedding2)
    return torch.dist(tensor1, tensor2).item()

def word_experiment():
    # structure for baseline sentence.
    clean_bl = preprocess_text(BASE_LINE)
    bl_embedding = generate_embeddings(clean_bl)
    bl_vector = bl_embedding["sentences"][0]["embedding"]
    # structure for other sentences
    data = generate_sentences()
    clean_data = preprocess_text(data)
    embeddings = generate_embeddings(clean_data)

    # Compute distances
    distances = {
        entry["sentence"]: compute_distances(entry["embedding"], bl_vector)
        for entry in embeddings["sentences"]
    }

    return distances

results = word_experiment()
print(results)