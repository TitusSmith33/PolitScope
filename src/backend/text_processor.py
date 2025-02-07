"""Pre-process text for NLP usage."""
from typing import Dict, Any
#import nltk
import re
from sentsplit.segment import SentSplit

#nltk.download()

def clean_sentence(sentence: str) -> str:
    """Clean a sentence by lowercasing and removing punctuation."""
    # Convert to lowercase
    sentence = sentence.lower()
    # Remove punctuation
    sentence = re.sub(r"[^\w\s]", "", sentence)
    # Remove extra spaces
    sentence = re.sub(r"\s+", " ", sentence).strip()
    return sentence

def preprocess_text(data: Dict[str, Any]) -> Dict[str, Any]:
    """Tokenize and clean a JSON object and preserve the original text."""
    # extract text from expected JSON input format
    if "content" not in data:
        raise ValueError("Input JSON must contain a 'content' key with the text.")
    text: str = data["content"]

    # split the data into sentences
    #raw_sentence = nltk.sent_tokenize(text)
    segmenter = SentSplit(lang="en")
    raw_sentence = segmenter.segment(text)

    # clean the sentences
    clean_text = []

    for sentence in raw_sentence:
        cleaned_sentence = clean_sentence(sentence)
        clean_text.append(cleaned_sentence)

    # using RoBERTa, initialize a tokenizer
    # reference: <https://huggingface.co/docs/transformers/en/model_doc/auto>
    # use_fast: utilized Rust implementation for processing large data faster
    # tokenizer = AutoTokenizer.from_pretrained("roberta-base", use_fast=True)
    # splits the input text into smaller units (tokens)
    # offset mapping ensures we have the original start/end location of tokens
    # tokens = tokenizer(text, return_offsets_mapping=True, add_special_tokens=False)

    # each token is decoded into its text representation, and its position in the original text is stored
    # token_data = []
    # for token, (start, end) in zip(tokens["input_ids"], tokens["offset_mapping"]):
        # decode token back to text
    #    token_text = tokenizer.decode([token]).strip()
    #    token_data.append({"token": token_text, "start": start, "end": end})

    # clean tokens (remove stop words, lowercasing, and remove punctuation)
    #cleaned_tokens = [
    #    t for t in token_data if t["token"].isalnum()
    #]

    # return original text and cleaned token data
    return {"original_text": text, "sentences": clean_text}
