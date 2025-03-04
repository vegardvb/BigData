# Correcting the approach to calculate Jaccard Similarities for each pair of sentences

# Sets of words for each sentence
sentence_1 = {"big", "data", "platform", "students", "blackboard"}
sentence_2 = {"questions", "minhash", "project", "ntnu", "students", "piazza"}
sentence_3 = {"ntnu", "big", "data", "platform", "blackboard", "piazza"}
sentence_4 = {"project", "data", "students", "blackboard", "piazza"}

# Function to calculate Jaccard Similarity
def jaccard_similarity(set_a, set_b):
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union

# Calculate Jaccard Similarity for all sentence combinations
jaccard_similarities = {
    "1-2": jaccard_similarity(sentence_1, sentence_2),
    "1-3": jaccard_similarity(sentence_1, sentence_3),
    "1-4": jaccard_similarity(sentence_1, sentence_4),
    "2-3": jaccard_similarity(sentence_2, sentence_3),
    "2-4": jaccard_similarity(sentence_2, sentence_4),
    "3-4": jaccard_similarity(sentence_3, sentence_4),
}

jaccard_similarities

print(jaccard_similarities)