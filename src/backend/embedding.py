"""Generate word embeddings using RoBERTa with confidence scoring."""

from typing import Dict, Any, List
import torch
import torch.nn.functional as tnnf
from transformers import AutoModel, AutoTokenizer

def generate_embeddings(data: Dict[str, Any]) -> Dict[str, Any]:
    """ Generate word embeddings for tokens."""
    # error handling
    # expected data format from text_processor.py
    if "tokens" not in data or "original_text" not in data:
        raise ValueError("Input dictionary must contain 'original_text' and 'tokens' keys.")
    
    # initialize variables, splitting the key and data
    original_text: str = data["original_text"]
    tokens: List[Dict[str, Any]] = data["tokens"]
    
    # load the pre-trained RoBERTa model and tokenizer
    # reference: <https://pypi.org/project/transformers/>
    model_name = "roberta-base"
    # use_fast: utilized Rust implementation for processing large data faster
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    model = AutoModel.from_pretrained(model_name)
    
    # Extract token texts and encode them for the model
    # initialize empty list
    token_texts = []
    # extract the token text(s)
    for token_dict in tokens:
        token_texts.append(token_dict["token"])
    # use the pre-trained RoBERTa tokenizer to encode the list of token strings
    # padding: padded to the same length so that they can be processed in batches
    # truncation: shortens tokenized sequences that exceed the model's maximum length
    # return_tensors: return the results as PyTorch tensors to be used directly in model
    encoded_inputs = tokenizer(token_texts, padding=True, truncation=True, return_tensors="pt")
    
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
    entropy = -torch.sum(probs * torch.log(probs + 1e-10), dim=1).tolist()
    
    # loop over each token, its corresponding embedding, and confidence score
    # and update the token dictionary with these values
    for token, embedding, conf_score in zip(tokens, embeddings_list, entropy):
        # add the embedding vector to the token dictionary
        token["embedding"] = embedding
        # add the confidence score to the token dictionary
        token["confidence_score"] = conf_score
    
    # return the dictionary containing the original text 
    # and the processed tokens with their embeddings and confidence scores
    return {"original_text": original_text, "tokens": tokens}