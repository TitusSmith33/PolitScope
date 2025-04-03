import pandas as pd
from fuzzywuzzy import fuzz

from embedding import generate_embeddings
from text_processor import preprocess_text
from comparison import compare_clusters

def confidence_validation():
    """Testing confidence coefficients one by one."""
    # Load dataset and take first 200 rows
    exp_path = "../../data/Political_Bias.csv"
    experiment_data = pd.read_csv(exp_path).head(10)

    # Extract the first sentence of each row
    def get_first_sentence(text):
        if isinstance(text, str):  # Ensure it's a string
            return text.split(".")[0]  # Take first sentence before the first period
        return ""

    experiment_data["Sentence"] = experiment_data["Text"].apply(get_first_sentence)

    correct_matches = 0  # Track how many we get right

    for _, row in experiment_data.iterrows():
        text = {"content": row["Sentence"]}  # Format for PolitScope
        clean_data = preprocess_text(text)
        example_output = generate_embeddings(clean_data)
        bias_sentences = compare_clusters(example_output)

        # If PolitScope identified it as bias AND it was labeled as bias (1), it's correct
        compared = fuzz.ratio(row["Sentence"], bias_sentences)
        print(f"ratio: {compared}")
        print()
        print(row["Sentence"])
        print()
        if compared >= 80 and row["Bias"] == 1:
            correct_matches += 1

    # Compute accuracy
    accuracy = (correct_matches / len(experiment_data)) * 100
    print(f"PolitScope Accuracy: {accuracy:.2f}%")

confidence_validation()
