"""Using PolitScope's trained model, analyze new input text."""

import pickle
import numpy as np
from typing import Dict, Any, List, Optional
from scipy.spatial.distance import cdist

CONFIDENCE_THRESHOLD = 0.85  
DISTANCE_WEIGHT = 0.7  
ENTROPY_WEIGHT = 0.3 

def compare_clusters(data: Dict[str, Any]) -> Optional[Dict[str, List[str]]]:
    """Compare new embeddings to the clusters in model."""
    # error handling
    if "sentences" not in data:
        raise ValueError("Input dictionary must contain 'sentences' key.")

    # open the model created in analysis.py
    with open("kmeans_model.pkl", "rb") as f:
        model_data = pickle.load(f)

    # grab specific aspects of the model
    print(f"DEBUG: Type of kmeans: {type(model_data)}")
    print()
    print("DEBUG: Loaded model_data keys:", model_data.keys())
    kmeans = model_data["kmeans"]
    print(type(kmeans))
    cluster_centers = model_data["cluster_centers"]

    # grab specific aspects of the new inputted text embeddings
    sentences = data["sentences"]
    embeddings = np.array([s["embedding"] for s in sentences])
    entropies = np.array([s["confidence_score"] for s in sentences])

    # perform the distance calculations for center of clusters
    # reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
    distances = cdist(embeddings, cluster_centers, metric='euclidean')
    print(distances)
    closest_clusters = np.argmin(distances, axis=1)
    min_distances = np.min(distances, axis=1)
    print("min_distance")
    print(min_distances)

    # clustered_sentences = {i: [] for i in range(len(cluster_centers))}
    # bias_classification = {}

    biased_sentences = []

    # use this formula to calculate confidence in clusters
    # confidence=0.7×(1−normalized distance)+0.3×(1−entropy score)
    for i, sentence in enumerate(sentences):
        cluster = closest_clusters[i]
        distance_score = 1 - (min_distances[i] / np.max(min_distances))
        entropy_score = 1 - (entropies[i] / np.max(entropies))

        confidence_score = (DISTANCE_WEIGHT * distance_score) + (ENTROPY_WEIGHT * entropy_score)
        is_confident = confidence_score >= CONFIDENCE_THRESHOLD

        if cluster == 1 and is_confident:
            biased_sentences.append(sentence["sentence"])

        print(f"\nSentence: {sentence['sentence']}")
        print(f"  → Assigned to Cluster {cluster}")
        print(f"  → Distance Score: {distance_score:.2f}, Entropy Score: {entropy_score:.2f}")
        print(f"  → Confidence Score: {confidence_score:.2f} ({'CONFIDENT' if is_confident else 'LOW CONFIDENCE'})")

        return {"biased_content": biased_sentences}