import json
from embedding import generate_embeddings
from text_processor import tokenize_and_clean


with open('dummy.json', 'r') as x:
    data = json.load(x)

def main():
    clean_data = tokenize_and_clean(data)
    example_output = generate_embeddings(clean_data)
    print(example_output)
    print(type(example_output))