"""Analyze sentence embeddings using K-Means clustering and save model for analysis use."""

from typing import Dict, Any
import numpy as np
import pickle
import json
from sklearn.cluster import KMeans

def analyze_embeddings(data: Dict[str, Any], k: int) -> None:
    """Cluster sentence embeddings using K-Means and save the model."""
    if "sentences" not in data:
        raise ValueError("Input dictionary must contain 'sentences' key.")
    
    sentences = data["sentences"]
    embeddings = np.array([s["embedding"] for s in sentences])
    print()
    print("Clustering step...")
    
    # apply K-Means clustering from sci-kit learn
    # n_clusters: amount of clusters needed -- may change this for experiments (3 or dynamic)
    # random_state: start with random centroids
    # n_init: kmeans runs multiple times with different initial centroids
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    # assign each embedding to a cluster
    clusters = kmeans.fit_predict(embeddings)

    print(kmeans.labels_)  # Shows which cluster each sentence was assigned

    
    # Group sentences by cluster
    clustered_sentences = {i: [] for i in range(k)}
    for sentence, cluster in zip(sentences, clusters):
        clustered_sentences[cluster].append(sentence["sentence"])

    # store model information including the cluster centers for distance comparison
    model_data = {
        "kmeans": kmeans,
        "cluster_centers": kmeans.cluster_centers_,
        "training_sentences": sentences
    }

    #print(model_data)
    #print("DEBUG: Final model_data before saving:", model_data)
    #print("DEBUG: Type of model_data:", type(model_data))
    #print("DEBUG: model_data keys:", model_data.keys() if isinstance(model_data, dict) else "N/A")

    # Save the model with all the information needed
    with open("kmeans_model.pkl", "wb") as f:
        pickle.dump(model_data, f)

    model_data_serializable = {
    "kmeans": {"n_clusters": model_data["kmeans"].n_clusters,  # Save only necessary attributes
               "random_state": model_data["kmeans"].random_state},
    "cluster_centers": model_data["cluster_centers"].tolist(),  # Convert NumPy array to list
    "training_sentences": model_data["training_sentences"]  # Already a list of dicts
}
    
    with open("debug_model_output.json", "w") as f:
        json.dump(model_data_serializable, f, indent=4)
    print("DEBUG: Model data saved to debug_model_output.json")
    
    print("DEBUG: Saved model_data keys:", model_data.keys()) 
    
    # Print sentences for manual analysis
    for cluster_id, cluster_sentences in clustered_sentences.items():
        print(f"\nCluster {cluster_id}:")
        for sentence in cluster_sentences[:10]:
            print(f" - {sentence}")
