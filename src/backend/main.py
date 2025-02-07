from embedding import generate_embeddings
from text_processor import preprocess_text


data ={"content": "This is a random sentence. Here is another one. politcal bias lives all around us and Trump is crazy #biden2028"}

def main():
    clean_data = preprocess_text(data)
    example_output = generate_embeddings(clean_data)
    print(example_output)
    print(type(example_output))
    print("1")

main()