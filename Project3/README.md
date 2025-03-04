# Project 3 - Mining Data Streams, AdWords, and Recommendation Systems

## Overview
This project is part of the TDT4305 - Big Data Architecture course and focuses on stream processing techniques, including DGIM, Bloom Filters, Flajolet-Martin, AdWords revenue optimization, and recommendation systems. It aims to build upon previous projects while introducing new algorithms relevant to data stream mining.

## Project Structure
```
/project3
    |-- Project 3 - Mining Data Streams, Adwords and RecSys.ipynb
    |-- Project 3- Mining Data Streams.pdf
    |-- data/
        |-- data_file.csv  (Contains user data stream samples)
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
   pip install numpy pandas
   ```

### Dataset Preparation
1. **Ensure the dataset is placed in the `/data/` directory.**
2. The dataset includes a CSV file (`data_file.csv`) containing a stream of user interactions.

## Tasks Breakdown

### Task 1: DGIM Algorithm (25 pts)
- Implement a DGIM algorithm to estimate the count of 1s in a sliding window.
- Optimize storage using logarithmic memory requirements.
- Implement a function to query specific window sizes.

### Task 2: Bloom Filters (20 pts)
- Implement a Bloom Filter to track seen usernames efficiently.
- Verify username availability and analyze false positives.

### Task 3: Flajolet-Martin Algorithm (10 pts)
- Implement an approximation algorithm for estimating unique visitors in a data stream.

### Task 4: AdWords Revenue Optimization (25 pts)
- Implement a **Greedy Algorithm** to maximize advertising revenue.
- Improve results using a **Balance Algorithm** for better competitive ratios.

### Task 5: Recommendation System (20 pts)
- Implement **User-User Collaborative Filtering** to predict user preferences.
- Implement **Item-Item Collaborative Filtering** for improved recommendation accuracy.

## Running the Code

### Running the Notebook
To execute all tasks, open and run the provided Jupyter Notebook:
```bash
jupyter notebook "Project 3 - Mining Data Streams, Adwords and RecSys.ipynb"
```

## Data Requirements
- Ensure the dataset (`data_file.csv`) is placed in the `/data` directory.
- The dataset must be accessible by the scripts for execution.

## Submission Guidelines
1. Ensure that the notebook runs without errors before submission.
2. Only include the Notebook file in a `.zip` file named `studentid_Project3_DGIM.zip`.
3. Upload the `.zip` file on Blackboard.
4. Include the names of all team members in the notebook.

## References
- [DGIM Algorithm](https://en.wikipedia.org/wiki/Datar-Gionis-Indyk-Motwani_algorithm)
- [Bloom Filters](https://en.wikipedia.org/wiki/Bloom_filter)
- [Flajolet-Martin Algorithm](https://en.wikipedia.org/wiki/Flajolet%E2%80%93Martin_algorithm)
- [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering)

Good luck!