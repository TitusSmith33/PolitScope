"""Pre-process text for NLP usage."""
from typing import Dict, Any
import re

def clean_sentence(sentence: str) -> str:
    """Clean a sentence by lowercasing and removing punctuation."""
    # Convert to lowercase
    sentence = sentence.lower()
    # Remove punctuation
    sentence = re.sub(r"[^\w\s]", "", sentence)
    # Remove extra spaces
    sentence = re.sub(r"\s+", " ", sentence).strip()
    return sentence

def split_into_sentences(text: str) -> list:
    """Split text into sentences using regex."""
    # regex pattern to split on `.`, `!`, or `?`, but keep them as part of the sentence.
    sentence_endings = r"(?<=[.!?])\s+"
    sentences = re.split(sentence_endings, text)
    
    # strip whitespace from each sentence and filter out empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    
    return sentences

def preprocess_text(data: Dict[str, Any]) -> Dict[str, Any]:
    """Tokenize and clean a JSON object and preserve the original text."""
    # extract text from expected JSON input format
    if "content" not in data:
        raise ValueError("Input JSON must contain a 'content' key with the text.")
    text: str = data["content"]

    # split the data into sentences
    raw_sentence = split_into_sentences(text)

    # clean the sentences
    clean_text = []

    for sentence in raw_sentence:
        cleaned_sentence = clean_sentence(sentence)
        clean_text.append(cleaned_sentence)

    # return original text and cleaned token data
    return {"original_text": text, "sentences": clean_text}
