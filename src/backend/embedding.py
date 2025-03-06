"""Generate word embeddings using RoBERTa with confidence scoring."""

from typing import Dict, Any
import torch
import torch.nn.functional as tnnf
from transformers import AutoModel, AutoTokenizer

def generate_embeddings(data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate word embeddings for tokens."""
    # error handling
    # expected data format from text_processor.py
    if "sentences" not in data or "original_text" not in data:
        raise ValueError("Input dictionary must contain 'original_text' and 'sentences' keys.")
    
    # initialize variables, splitting the key and data
    original_text = data["original_text"]
    sentences = data["sentences"]
    
    # load the pre-trained RoBERTa model and tokenizer
    # reference: <https://pypi.org/project/transformers/>
    print("embedding step")
    model_name = "roberta-base"
    # use_fast: utilized Rust implementation for processing large data faster
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModel.from_pretrained(model_name)
    
    # batching to handle the memory errors encountered
    # handle chunks of the data at a time rather than feeding the whole thing at once
    batch_size = 64
    sentence_data = []
    for i in range(0, len(sentences), batch_size):
        batch = sentences[i:i + batch_size]
        encoded_inputs = tokenizer(batch, padding=True, truncation=True, return_tensors="pt")
    # disables gradient calculation to save memory
    # feed the tokenized input into the model to generate outputs
        with torch.no_grad():
            outputs = model(**encoded_inputs)
    
    # create a single embedding vector for the whole input sequence
    # convert the PyTorch tensor of embeddings into a Python list 
        embeddings = outputs.last_hidden_state.mean(dim=1)
        embeddings_list = embeddings.tolist()
    
    # convert the embeddings into probabilities
    # calculate the entropy for each sequence of embeddings to measure the confidence of the predictions
    # reference: <https://pytorch.org/docs/stable/nn.functional.html>
        probs = tnnf.softmax(embeddings, dim=1)
        entropy = torch.sum(probs * torch.log(probs + 1e-10), dim=1).tolist()
    
    # Create the structured output
        for sentence, embedding, conf_score in zip(batch, embeddings_list, entropy):
            sentence_data.append({
                "sentence": sentence,
                "embedding": embedding,
                "confidence_score": conf_score
            })
    
    # return the dictionary containing the original text 
    # and the processed tokens with their embeddings and confidence scores
    return {"original_text": original_text, "sentences": sentence_data}