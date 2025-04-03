import torch
import matplotlib.pyplot as plt
from text_processor import preprocess_text
from embedding import generate_embeddings

# Constants
BASE_LINE = {"content": "Donald Trump is a great president."}

subjects = [
    "Donald Trump", "Joe Biden", "Ron Cole", "The mayor", "Anakan Skywalker", 
    "Barack Obama", "Hillary Clinton", "Elon Musk", "The teacher", "The president", 
    "Vladimir Putin", "Oprah Winfrey", "Tom Hanks", "LeBron James", 
    "Albert Einstein", "Nelson Mandela", "The Dalai Lama", "Warren Buffet", 
    "Jeff Bezos", "Bill Gates", "Steve Jobs", "Taylor Swift", "Beyoncé", "Rihanna", 
    "Kim Kardashian", "Dwayne 'The Rock' Johnson", "Ellen DeGeneres", 
    "Mark Zuckerberg"
]

adjectives = [
    "great", "honest", "intelligent", "charismatic", "dynamic", 
    "courageous", "inspiring", "influential", "dedicated", "compassionate", 
    "ambitious", "creative", "innovative", "visionary", "talented", 
    "hardworking", "persistent", "brave", "focused", "humble", 
    "respectful", "generous", "trustworthy", "strong", "outspoken",
    "neutral", "mature", "calm", "objective", "balanced", 
    "reasonable", "methodical", "pragmatic", "reliable", "logical", 
    "practical", "unbiased", "steady", "thoughtful", "sensible", 
    "corrupt", "terrible", "controversial", "selfish", "greedy", 
    "dishonest", "lazy", "unfocused", "unreliable", "arrogant", 
    "irresponsible", "ignorant", "vindictive", "disrespectful"
]

nouns = [
    "president", "leader", "golfer", "Jedi", "role model", 
    "actor", "entrepreneur", "scientist", "philanthropist", "author", 
    "coach", "musician", "activist", "visionary", "comedian", 
    "inventor", "teacher", "journalist", "investor", "director", 
    "producer", "diplomat", "athlete", "social worker", "artist", 
    "designer", "architect", "psychologist", "filmmaker"
]

def generate_sentences():
    """Generate sentences with one difference from the baseline."""
    baseline_subject = "Donald Trump"
    baseline_adjective = "great"
    baseline_noun = "president"
    
    sentences = []

    # Change only the subject
    for subject in subjects:
        if subject != baseline_subject:
            sentences.append(f"{subject} is a {baseline_adjective} {baseline_noun}.")

    # Change only the adjective
    for adjective in adjectives:
        if adjective != baseline_adjective:
            sentences.append(f"{baseline_subject} is a {adjective} {baseline_noun}.")

    # Change only the noun
    for noun in nouns:
        if noun != baseline_noun:
            sentences.append(f"{baseline_subject} is a {baseline_adjective} {noun}.")
    
    return sentences


def compute_distances(embedding1, embedding2):
    """Compute Euclidean distance between two embeddings."""
    tensor1 = torch.tensor(embedding1)
    tensor2 = torch.tensor(embedding2)
    return torch.dist(tensor1, tensor2).item()


def word_experiment():
    # Generate all sentences
    all_sentences = generate_sentences()

    # Preprocess baseline sentence
    clean_bl = preprocess_text(BASE_LINE)
    bl_embedding = generate_embeddings(clean_bl)
    bl_vector = bl_embedding["sentences"][0]["embedding"]

    # Preprocess and embed the sentences to compute distances
    clean_data = preprocess_text({"content": " ".join(all_sentences)})
    embeddings = generate_embeddings(clean_data)

    # Compute distances for all sentences from baseline
    distances = {
        entry["sentence"]: compute_distances(entry["embedding"], bl_vector)
        for entry in embeddings["sentences"]
    }

    # Categorize sentences
    same_subject = []
    different_subject = []
    same_adjective = []
    different_adjective = []
    same_noun = []
    different_noun = []

    # Categorize based on the subject, adjective, and noun
    for sentence, distance in distances.items():
        if "donald trump" in sentence:
            same_subject.append((sentence, distance))
        else:
            different_subject.append((sentence, distance))

        if "great" in sentence:
            same_adjective.append((sentence, distance))
        else:
            different_adjective.append((sentence, distance))

        if "president" in sentence:
            same_noun.append((sentence, distance))
        else:
            different_noun.append((sentence, distance))

    # Create a bar chart for the average distances of each category

    ##TODO:  ADD error lines
    categories = ['Same Subject', 'Different Subject', 'Same Adjective', 'Different Adjective', 'Same Noun', 'Different Noun']
    same_subject_distances = [dist for sentence, dist in same_subject]
    different_subject_distances = [dist for sentence, dist in different_subject]
    same_adjective_distances = [dist for sentence, dist in same_adjective]
    different_adjective_distances = [dist for sentence, dist in different_adjective]
    same_noun_distances = [dist for sentence, dist in same_noun]
    different_noun_distances = [dist for sentence, dist in different_noun]

    avg_distances = [
    sum(same_subject_distances) / len(same_subject_distances) if same_subject_distances else 0,
    sum(different_subject_distances) / len(different_subject_distances) if different_subject_distances else 0,
    sum(same_adjective_distances) / len(same_adjective_distances) if same_adjective_distances else 0,
    sum(different_adjective_distances) / len(different_adjective_distances) if different_adjective_distances else 0,
    sum(same_noun_distances) / len(same_noun_distances) if same_noun_distances else 0,
    sum(different_noun_distances) / len(different_noun_distances) if different_noun_distances else 0
]
    
    # Create the bar graph
    ## plt.errorbar (x,y, stand error of mean)
    plt.figure(figsize=(10, 6))
    plt.bar(categories, avg_distances, color=['cyan', 'navy', 'lightcoral', 'darkred', 'lightgreen', 'seagreen'])
    plt.xlabel('Categories')
    plt.ylabel('Average Distance')
    plt.title('Average Euclidean Distances for Each Category')
    plt.xticks(rotation=45, ha='right')
    plt.ylim(1.5, 2.75)
    plt.tight_layout()

    # Show the plot
    plt.savefig("average_distances_bar_graph.png")

# Run the experiment
word_experiment()
