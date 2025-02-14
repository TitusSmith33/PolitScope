"""Analyze sentence embeddings using K-Means clustering."""

from typing import Dict, Any
import numpy as np
import pickle
from sklearn.cluster import KMeans

def analyze_embeddings(data: Dict[str, Any], k: int) -> Dict[str, Any]:
    """Cluster sentence embeddings using K-Means."""
    if "sentences" not in data:
        raise ValueError("Input dictionary must contain 'sentences' key.")
    
    sentences = data["sentences"]
    embeddings = np.array([s["embedding"] for s in sentences])
    print("clustering step")
    
    # apply K-Means clustering from sci-kit learn
    # n_clusters: amount of clusters needed -- may change this for experiments (3 or dynamic)
    # random_state: start with random centroids
    # n_init: kmeans runs multiple times with different initial centroids
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    # assign each embedding to a cluster
    clusters = kmeans.fit_predict(embeddings)
    
    # Group sentences by cluster
    clustered_sentences = {i: [] for i in range(k)}
    for sentence, cluster in zip(sentences, clusters):
        clustered_sentences[cluster].append(sentence["sentence"])

    # Save the trained model
    with open("kmeans_model.pkl", "wb") as f:
        pickle.dump(kmeans, f)
    
    # Print sentences for manual analysis
    for cluster_id, cluster_sentences in clustered_sentences.items():
        print(f"\nCluster {cluster_id}:")
        for sentence in cluster_sentences[:20]:
            print(f" - {sentence}")
    
    return {"original_text": data["original_text"], "sentences": sentences}
