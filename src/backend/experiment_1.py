import pandas as pd
from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt

from embedding import generate_embeddings
from text_processor import preprocess_text
from comparison import compare_clusters

def confidence_validation():
    """Testing confidence coefficients one by one."""
    # load dataset and take first 200 rows
    exp_path = "../../data/Political_Bias.csv"
    experiment_data = pd.read_csv(exp_path).dropna().head(200)

    # Extract the first sentence of each row
    def get_first_sentence(text):
        if isinstance(text, str):
            # we had to do this because PolitScope handles text largely, so in order to compare
            # each row to the data that PolitScope spits out, we had to take only the first
            # sentence of each row in the labeled data.
            return text.split(".")[0]
        return ""

    experiment_data["Sentence"] = experiment_data["Text"].apply(get_first_sentence)

    # track how many matches we get to the labeled dataset
    TP, FN, TN, FP = 0, 0, 0, 0

    for _, row in experiment_data.iterrows():
        # format text for what PolitScope is expecting
        text = {"content": row["Sentence"]}
        clean_data = preprocess_text(text)
        example_output = generate_embeddings(clean_data)
        bias_sentences = compare_clusters(example_output)

        # if PolitScope identified it as bias AND it was labeled as bias (1) in labeled dataset, it's correct
        # use fuzz because of cleaning so not exact match
        compared = fuzz.ratio(row["Sentence"], bias_sentences)

        # PolitScope detects it as biased
        detected_as_bias = compared >= 75

        # expected label from dataset
        actual_bias = row["Bias"] == 1 
        # correctly detected bias
        if detected_as_bias and actual_bias:
            TP += 1 
        # missed a biased sentence (false negative)
        elif not detected_as_bias and actual_bias:
            FN += 1
        # correctly identified neutral (true negative)
        elif not detected_as_bias and not actual_bias:
            TN += 1
        # Wrongly marked neutral as biased (false positive)
        elif detected_as_bias and not actual_bias:
            FP += 1

    # Compute accuracy and other metrics
    accuracy = (TP + TN) / (TP + TN + FP + FN) * 100 if (TP + TN + FP + FN) > 0 else 0
    precision = TP / (TP + FP) * 100 if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) * 100 if (TP + FN) > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Print results
    print(f"PolitScope Accuracy: {accuracy:.2f}%")
    print(f"Precision: {precision:.2f}% (How often PolitScope is correct when it says bias)")
    print(f"Recall: {recall:.2f}% (How well PolitScope catches actual bias)")
    print(f"F1 Score: {f1_score:.2f}% (Balance between precision & recall)")

#confidence_validation()

# data from running experiment 1
f1_scores = {
    "90 (D)/ 10 (E)": 0.00,
    "80 (D)/ 20 (E)": 0.00,
    "70 (D)/ 30 (E)": 0.00,
    "60 (D)/ 40 (E)": 0.00,
    "50 (D)/ 50 (E)": 3.97,
    "40 (D)/ 60 (E)": 19.16,
    "30 (D)/ 70 (E)": 45.71,
    "20 (D)/ 80 (E)": 58.46,
    "10 (D)/ 90 (E)": 60.52,
}

# separate labels and values
ratios = list(f1_scores.keys())
scores = list(f1_scores.values())

def create_graph():
    """Create line graph."""
    plt.figure(figsize=(10, 6))
    plt.plot(ratios, scores, marker='o', linestyle='-', color='blue')
    plt.title("PolitScope's Accuracy Based on Confidence Coefficients")
    plt.xlabel("Distance(D) / Entropy(E) Ratio")
    plt.ylabel("F1 Score % (Accuracy)")
    plt.grid(True)
    plt.ylim(0, 70)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # save graph
    plt.savefig("confidence_graph.png")

create_graph()
