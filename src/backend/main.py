from embedding import generate_embeddings
from text_processor import preprocess_text
from analysis import analyze_embeddings


data ={"content": "Trump is my favorite president, and I really like that he won the election. this is a normal sentence with no impact. I am adding random sentences. this is just an example sentence. politcal bias lives all around us and Trump is crazy #biden2028. I think democrats are the smartest voters in the country. I think republicans and people that vote for trump are the smartest voters in the world."}

def main():
    clean_data = preprocess_text(data)
    example_output = generate_embeddings(clean_data)
    #print(example_output)
    #print(type(example_output))
    #print("1")
    num_clusters = 2
    analyze_embeddings(example_output, num_clusters)


main()