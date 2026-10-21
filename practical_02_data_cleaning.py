"""
DS-505 Practical: Data Hygiene, Missing Values, Deduplication and Renaming
Simple student-friendly program based on the uploaded workbook.
"""

import pandas as pd
import numpy as np

# Step 1: Create a dataset with missing values and duplicate records
raw_data = {
    'cust_id': [1, 2, 3, 4, 5, 2, 6, 7],
    'cust_name': ['Amit', 'Pooja', 'Rahul', 'Sneha', 'Vikram', 'Pooja', 'Karan', 'Neha'],
    'age': [25, 30, np.nan, 22, 28, 30, np.nan, 35],
    'monthly_income': [45000, 52000, 61000, np.nan, 48000, 52000, 55000, 70000]
}

df = pd.DataFrame(raw_data)
print("--- ORIGINAL DATASET ---")
print(df)

# Step 2: Check missing values per column
print("\n--- MISSING VALUE COUNT PER COLUMN ---")
print(df.isna().sum())

# Step 3: Remove duplicate records
df_dedup = df.drop_duplicates()
print(f"\n--- AFTER DEDUPLICATION (Rows removed: {len(df) - len(df_dedup)}) ---")
print(df_dedup)

# Step 4: Impute missing numerical values (Age with median, Income with mean)
df_clean = df_dedup.copy()
median_age = df_clean['age'].median()
mean_income = df_clean['monthly_income'].mean()

df_clean['age'] = df_clean['age'].fillna(median_age)
df_clean['monthly_income'] = df_clean['monthly_income'].fillna(mean_income)

# Step 5: Rename columns to clear professional names
df_clean = df_clean.rename(columns={
    'cust_id': 'Customer_ID',
    'cust_name': 'Full_Name',
    'age': 'Age',
    'monthly_income': 'Monthly_Income_INR'
})

print("\n--- FINAL CLEANED & RENAMED DATASET ---")
print(df_clean)
print("\nRemaining missing values:", df_clean.isna().sum().sum())
