from fuzzywuzzy import fuzz, process
from typing import Dict, List, Optional
import re

def find_similar_bias_sentences(input_data, bias_data, threshold=70) -> Optional[Dict[str, List[str]]]:
    content_text = input_data.get("content", "")
    bias_list = bias_data.get("bias_content", [])

    if not isinstance(bias_list, list):
        return {"bias_content": []}

    # Split input content into sentences
    input_sentences = re.split(r'(?<=[.!?]) +', content_text)

    matched_sentences = []

    for bias_sentence in bias_list:
        result = process.extractOne(
            bias_sentence, input_sentences, scorer=fuzz.token_set_ratio
        )

        if result:
            best_match, score = result
            if score >= threshold:
                matched_sentences.append(best_match)
            else:
                matched_sentences.append("")
        else:
            matched_sentences.append("")

    return {"bias_content": matched_sentences}