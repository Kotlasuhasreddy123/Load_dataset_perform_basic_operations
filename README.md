F500 Data Loading and Basic Operations

This repository demonstrates fundamental data science operations using the Fortune 500 (F500) dataset, focusing on initial data loading, statistical summaries, and data visualization.

The core Python script is named Load dataset & perform basic operations.py.

Key Functionality

Data Loading: Successfully loads the local f500.csv file into a Pandas DataFrame.

Statistical Summary: Calculates and prints the mean profit and generates descriptive statistics using Pandas and NumPy.

Feature Engineering: Calculates a new column, rank_change, by subtracting the current rank from the previous rank.

Data Visualization: Generates a histogram of the company revenues using Matplotlib to show the data distribution.

Visualization Result

The histogram below illustrates the distribution of company revenues, showing that most companies fall into the lower revenue brackets while a few outliers have extremely high revenues.
