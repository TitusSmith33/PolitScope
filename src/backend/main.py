"""Communicate with frontend and driver of backend."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict
import pandas as pd

from embedding import generate_embeddings
from text_processor import preprocess_text
from analysis import analyze_embeddings
from comparison import compare_clusters
from mapping import find_similar_bias_sentences

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; specify in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_and_combine_text(csv_file: str) -> Dict[str, Any]:
    """Load text data from a CSV file and combine all rows into a single text block."""
    df = pd.read_csv(csv_file)
    if "cleaned_content" not in df.columns:
        raise ValueError("CSV must contain a 'text' column.")
    
    # sample only a fraction of the dataset
    # 500 works (~15 min)
    sampled_df = df.head(500)
    
    # combine all text entries into one
    combined_text = " ".join(sampled_df["cleaned_content"].astype(str))
    return {"content": combined_text}

class TextInput(BaseModel):
    content: str

def main():
    """Function for adding more test data to model."""
    # testing data
    csv_file = "../../data/PolitScope_Data.csv"
    raw_text = load_and_combine_text(csv_file)   
    clean_data = preprocess_text(raw_text)
    example_output = generate_embeddings(clean_data)

    num_clusters = 2
    analyze_embeddings(example_output, num_clusters)
    
    #compare_clusters(example_output)

## For communicating with frontend and extension
## RUN IN TERMINAL: uvicorn main:app --reload

@app.post("/analyze")
def analyze_text(data: TextInput) -> Dict[str, Any]:
    try:
        # prepare the data for embedding step
        clean_data = preprocess_text(data.dict())
        print(clean_data)
        # embed the text from webpage
        embeddings = generate_embeddings(clean_data)
        # compare the clusters up to model
        bias_result = compare_clusters(embeddings)
        # return dict of bias content
        #print(bias_result)
        formatted_result = find_similar_bias_sentences(data.dict(), bias_result)
        print(formatted_result)
        print(type(formatted_result))
        #return bias_result
        return formatted_result
    # error handling
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# main()
