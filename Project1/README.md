# Project 1 - Introduction to Apache Spark

## Overview
This project is part of the TDT4305 - Big Data Architecture course and serves as an introduction to Apache Spark, a distributed computing framework for large-scale data processing. It includes five tasks, covering schema definition, SQL queries, graph structures, and machine learning with Spark MLib.

## Project Structure
```
/project1
    |-- Task1.ipynb
    |-- Task2.ipynb
    |-- Task3.ipynb
    |-- Task4.ipynb
    |-- Project 1- Introduction to Apache Spark.pdf
    |-- data/
        |-- badges_csv.gz
        |-- comments_csv.gz
        |-- posts_csv.gz
        |-- users_csv.gz
```

## Setup Instructions

### Databricks Setup
1. **Login to Databricks Community Edition:**
   - Visit [Databricks Community Edition](https://community.cloud.databricks.com/login.html)
   - Upload dataset files from `data/` folder.
   - Import the notebooks (`Task1.ipynb`, `Task2.ipynb`, etc.) into Databricks.

### Spark Setup (Linux)
1. **Download and Install Apache Spark:**
   ```bash
   wget https://downloads.apache.org/spark/spark-3.3.4/spark-3.3.4-bin-hadoop3.tgz
   tar xfz spark-3.3.4-bin-hadoop3.tgz
   sudo mv spark-3.3.4-bin-hadoop3 /usr/local/spark
   ```
2. **Update Environment Variables:**
   ```bash
   echo 'export PATH=$PATH:/usr/local/spark/bin' >> ~/.bashrc
   source ~/.bashrc
   ```
3. **Verify Spark Installation:**
   ```bash
   spark-shell
   ```

## Tasks Breakdown

### Task 1: Data Schema and Loading (20 pts)
- Define schema for structured datasets.
- Implement helper functions to load CSV files into Spark DataFrames.
- Validate the schema implementation.

### Task 2: SQL Queries with Spark (20 pts)
- Implement SQL queries to extract insights from the dataset.
- Run queries using Spark SQL functions.
- Validate the query outputs.

### Task 3: Data Analysis and Correlation (20 pts)
- Compute Pearson correlation coefficient.
- Construct a tag graph and extract relationships between tags.
- Validate the implementations.

### Task 4: Expert User Analysis (20 pts)
- Analyze user expertise levels based on reputation scores.
- Compute correlation between expertise and topic diversity.
- Answer conceptual questions about Apache Spark.

### Task 5: Machine Learning with Spark MLib (20 pts)
- Implement a linear regression model to predict biomass.
- Train and test the model on fermentation data.
- Compute RMSE (Root Mean Squared Error) for evaluation.

## Data Requirements
- Ensure the dataset files (`badges_csv.gz`, `comments_csv.gz`, `posts_csv.gz`, `users_csv.gz`) are placed in the `/data` directory.
- The dataset must be uploaded to the Databricks environment for execution.

## Submission Guidelines
1. Ensure that the notebook runs without errors before submission.
2. Only include the `.ipynb` files in a `.zip` file named `Project1_Spark.zip`.
3. Upload the `.zip` file on Blackboard.
4. Include the names of all team members in each notebook.

## References
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Databricks Community Edition](https://community.cloud.databricks.com/login.html)
- [Pearson Correlation Explanation](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)

Good luck!