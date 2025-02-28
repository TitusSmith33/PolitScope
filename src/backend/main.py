from embedding import generate_embeddings
from text_processor import preprocess_text
from analysis import analyze_embeddings
from typing import Any, Dict
import pandas as pd

def load_and_combine_text(csv_file: str) -> Dict[str, Any]:
    """Load text data from a CSV file and combine all rows into a single text block."""
    df = pd.read_csv(csv_file)
    if "cleaned_content" not in df.columns:
        raise ValueError("CSV must contain a 'text' column.")
    
    # Sample only a fraction of the dataset
    # 50% of the data
    # sampled_df = df.sample(frac=0.001, random_state=42)
    sampled_df = df.head(5)
    
    combined_text = " ".join(sampled_df["cleaned_content"].astype(str))  # Combine all text entries into one
    return {"content": combined_text}


#data ={"content": "Trump is my favorite president, and I really like that he won the election. this is a normal sentence with no impact. I am adding random sentences. this is just an example sentence. politcal bias lives all around us and Trump is crazy #biden2028. I think democrats are the smartest voters in the country. I think republicans and people that vote for trump are the smartest voters in the world."}

def main():
    csv_file = "../../data/PolitScope_Data.csv"
    print(csv_file)
    raw_text = load_and_combine_text(csv_file)
    # print(raw_text)
    clean_data = preprocess_text(raw_text)
    print(clean_data)
    example_output = generate_embeddings(clean_data)
    #print(example_output)
    #print(type(example_output))
    print("embedding complete")
    num_clusters = 20
    analyze_embeddings(example_output, num_clusters)
    print("1")


main()