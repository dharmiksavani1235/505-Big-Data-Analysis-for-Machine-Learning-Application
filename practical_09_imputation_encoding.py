"""
DS-505 Practical: Missing Value Imputation and Categorical Encoding
Simple student-friendly program based on the uploaded workbook.
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Step 1: Create raw dataset with missing values and categorical features
raw_data = {
    'Applicant_ID': [101, 102, 103, 104, 105, 106],
    'Credit_Score': [710, np.nan, 680, 750, np.nan, 620],
    'Income_k': [55.0, 62.0, np.nan, 80.0, 48.0, 50.0],
    'Education': ['Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'Bachelors'],
    'Loan_Approved': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No']
}
df = pd.DataFrame(raw_data)
print("--- ORIGINAL DATASET ---")
print(df)

# Step 2: Handle Missing Numerical Values with SimpleImputer
imputer = SimpleImputer(strategy='mean')
df[['Credit_Score', 'Income_k']] = imputer.fit_transform(df[['Credit_Score', 'Income_k']])

# Step 3: Encode Target Variable using LabelEncoder
le = LabelEncoder()
df['Loan_Approved_Encoded'] = le.fit_transform(df['Loan_Approved'])

# Step 4: One-Hot Encode 'Education' category
df_encoded = pd.get_dummies(df, columns=['Education'], prefix='Edu', drop_first=False)

print("\n--- PROCESSED & ENCODED MACHINE LEARNING READY DATASET ---")
print(df_encoded.drop(columns=['Loan_Approved']))
print(f"\nLabelEncoder Mapping: {dict(zip(le.classes_, le.transform(le.classes_)))}")
