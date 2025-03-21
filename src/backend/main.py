"""Communicate with frontend and driver of backend."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
import pandas as pd

from embedding import generate_embeddings
from text_processor import preprocess_text
from analysis import analyze_embeddings
from comparison import compare_clusters

app = FastAPI()

# def load_and_combine_text(csv_file: str) -> Dict[str, Any]:
    #"""Load text data from a CSV file and combine all rows into a single text block."""
    #df = pd.read_csv(csv_file)
    #if "cleaned_content" not in df.columns:
    #    raise ValueError("CSV must contain a 'text' column.")
    
    # Sample only a fraction of the dataset
    # 50% of the data
    #### sampled_df = df.sample(frac=0.001, random_state=42)
    #sampled_df = df.head(5)
    
    #combined_text = " ".join(sampled_df["cleaned_content"].astype(str))  # Combine all text entries into one
    #return {"content": combined_text}


# data ={"content": "Trump is my favorite president, and I really like that he won the election. this is a normal sentence with no impact. I am adding random sentences. this is just an example sentence. politcal bias lives all around us and Trump is crazy #biden2028. I think democrats are the smartest voters in the country. I think republicans and people that vote for trump are the smartest voters in the world."}

class TextInput(BaseModel):
    content: str

#def main():
    # csv_file = "../../data/PolitScope_Data.csv"
    # raw_text = load_and_combine_text(csv_file)   
    
    # raw_text = data
    # clean_data = preprocess_text(raw_text)
    # example_output = generate_embeddings(clean_data)

    # print("embedding complete")

    # num_clusters = 2
    # analyze_embeddings(example_output, num_clusters)
    
    #compare_clusters(example_output)

## RUN IN TERMINAL: uvicorn main:app --reload

@app.post("/analyze")
def analyze_text(data: TextInput) -> Dict[str, Any]:
    try:
        # prepare the data for embedding step
        clean_data = preprocess_text(data.dict())
        # embed the text from webpage
        embeddings = generate_embeddings(clean_data)
        # compare the clusters up to model
        bias_result = compare_clusters(embeddings)
        # return dict of bias content
        return bias_result
    # error handling
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
