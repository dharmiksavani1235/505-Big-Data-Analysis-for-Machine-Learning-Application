"""
DS-505 Practical: Dataset Ingestion, Inspection and Descriptive Statistics
Simple student-friendly program based on the uploaded workbook.
"""

import pandas as pd
import numpy as np

# Step 1: Create a representative customer sales dataset
data = {
    'Transaction_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_Name': ['Aarav', 'Diya', 'Rohan', 'Ananya', 'Vivaan', 'Isha', 'Kabir', 'Meera', 'Aditya', 'Sanya'],
    'Age': [28, 34, 22, 45, 31, 29, 52, 26, 38, 41],
    'Department': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Electronics', 'Home'],
    'Purchase_Amount': [12500.50, 4200.00, 18900.75, 3100.25, 6500.00, 14200.00, 8900.50, 5100.00, 22400.00, 7800.25],
    'Satisfaction_Score': [4.5, 3.8, 4.9, 3.2, 4.0, 4.7, 3.5, 4.2, 4.8, 3.9]
}

df = pd.DataFrame(data)

# Step 2: Inspect DataFrame structure
print("--- FIRST 5 RECORDS (head) ---")
print(df.head())

print("\n--- LAST 5 RECORDS (tail) ---")
print(df.tail())

print("\n--- DATASET SHAPE (Rows, Columns) ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATASET INFORMATION & DTYPES ---")
df.info()

print("\n--- DESCRIPTIVE SUMMARY STATISTICS ---")
print(df.describe(include='all'))
