# Project 2 - Finding Similar News Articles

## Overview
This project is part of the TDT4305 - Big Data Architecture course and focuses on text similarity detection. The goal is to find similar BBC news articles using techniques such as Shingling, Jaccard Similarity, MinHash, and Locality Sensitive Hashing (LSH) to efficiently identify articles discussing the same events.

## Project Structure
```
/project2
    |-- MinHash.ipynb
    |-- lsh.py
    |-- Project 2- Finding Similar News Articles.pdf
    |-- data/
        |-- bbc/  (Contains 2225 BBC news articles as .txt files)
```

## Setup Instructions

### Python Environment Setup
1. **Ensure Python 3.8 or newer is installed.**
2. **Recommended:** Create a virtual environment and install dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install required packages:**
   ```bash
   pip install numpy
   ```

### Dataset Preparation
1. **Ensure the dataset is placed in the `/data/bbc/` directory.**
2. The `bbc/` folder contains 2225 `.txt` documents from BBC News (2004-2005).

## Tasks Breakdown

### Task 1: Creating k-Shingles
- Implement document representation using k-shingles.
- Extract k-shingles from each document.

### Task 2: Constructing the Input Matrix
- Generate signature sets for the documents based on k-shingles.

### Task 3: MinHash Signature Matrix
- Implement MinHash to generate a signature matrix.
- Create random hash functions using prime coefficients.

### Task 4: Locality Sensitive Hashing (LSH)
- Implement LSH to find candidate pairs efficiently.
- Use bands and row hashing to cluster similar documents.

### Task 5: Compute Similarities Above Threshold
- Compare candidate document pairs to determine similarity.
- Filter document pairs with similarity above a defined threshold `t`.

## Running the Code

### Running MinHash Implementation
To execute the MinHash algorithm, run:
```bash
python MinHash.ipynb
```

### Running the LSH Algorithm
To run the LSH implementation, execute:
```bash
python lsh.py
```

## Data Requirements
- Ensure the dataset (`bbc/`) is placed in the `/data` directory.
- The dataset must be accessible by the scripts for execution.

## Submission Guidelines
1. Ensure that all scripts run without errors before submission.
2. Only include the `.py` file, Notebook, and Report PDF in a `.zip` file named `student_id_Project2_LSH.zip`.
3. Upload the `.zip` file on Blackboard.
4. Include the names of all team members in the notebook and report.

## References
- [BBC News Dataset](https://www.bbc.co.uk/news)
- [MinHash Algorithm](https://en.wikipedia.org/wiki/MinHash)
- [Locality Sensitive Hashing](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)

Good luck!
