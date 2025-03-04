import numpy as np

# Input matrix
input_matrix = np.array([
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 1]
])

# Permutations specified
permutations = [
    np.array([4, 5, 6, 7, 8, 9, 0, 1, 2, 3]),  # H1 - Adjusted for 0-based indexing
    np.array([8, 5, 2, 9, 6, 3, 0, 7, 4, 1]),  # H2
    np.array([9, 6, 3, 0, 7, 4, 1, 8, 5, 2])   # H3
]

# Function to compute the MinHash signature matrix using permutations
def compute_minhash_with_permutations(input_matrix, permutations):
    num_docs = input_matrix.shape[1]
    num_perms = len(permutations)
    signature_matrix = np.full((num_perms, num_docs), np.inf)
    
    for perm_idx, perm in enumerate(permutations):
        permuted_matrix = input_matrix[perm, :]  # Apply permutation
        for doc_idx in range(num_docs):
            for row_idx in range(len(perm)):
                if permuted_matrix[row_idx, doc_idx] == 1:
                    signature_matrix[perm_idx, doc_idx] = min(signature_matrix[perm_idx, doc_idx], row_idx)
                    break  # Stop at the first '1' in the permuted column for this document
    return signature_matrix

# Compute the MinHash signature matrix
signature_matrix = compute_minhash_with_permutations(input_matrix, permutations)

print("MinHash Signature Matrix:")
print(signature_matrix)



import numpy as np

# Input matrix as provided
input_matrix = np.array([
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
])
# Assume hash_1, hash_2, and hash_3 are defined as shown in the previous snippet
hash_1 = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
hash_2 = [9, 6, 3, 10, 7, 4, 1, 8, 5, 2]
hash_3 = [10, 7, 4, 1, 8, 5, 2, 9, 6, 3]

# Converting hash values to 0-based indexing for Python
hash_1 = [x-1 for x in hash_1]
hash_2 = [x-1 for x in hash_2]
hash_3 = [x-1 for x in hash_3]

# Compile the hash arrays into a list for easier iteration
hash_lists = [hash_1, hash_2, hash_3]

# Initialize Sig_M with infinite values
Sig_M = np.full((3, 4), np.inf)

# Compute the Sig_M using the predefined hash arrays
for i, hash_list in enumerate(hash_lists):
    for j in range(Sig_M.shape[1]):  # For each sentence
        hash_values = [hash_list[index] for index, value in enumerate(input_matrix[:, j]) if value == 1]
        if hash_values:  # If the list is not empty
            Sig_M[i, j] = min(hash_values)

Sig_M = Sig_M.astype(int)
print("Updated MinHash Signature Matrix using predefined hash arrays:")
print(Sig_M)

def jaccard_similarity(Sig_M, i, j):
    return np.sum(Sig_M[:, i] == Sig_M[:, j]) / Sig_M.shape[0]

for i in range(Sig_M.shape[1]):
    for j in range(i + 1, Sig_M.shape[1]):
        print(f"Jaccard Similarity between Sentence {i + 1} and Sentence {j + 1} is {jaccard_similarity(Sig_M, i, j)}")
        