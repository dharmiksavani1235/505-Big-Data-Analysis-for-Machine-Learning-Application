"""
DS-505 Practical: Feature Scaling and Train-Test Split
Simple student-friendly program based on the uploaded workbook.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Step 1: Create feature matrix X and target y
np.random.seed(42)
X = pd.DataFrame({
    'Feature_Age': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Feature_Salary': [25000, 32000, 48000, 55000, 62000, 71000, 85000, 92000, 110000, 130000]
})
y = np.array([0, 0, 0, 1, 0, 1, 1, 1, 1, 1])

print("--- ORIGINAL FEATURE VALUES ---")
print(X)

# Step 2: Apply StandardScaler (Mean=0, Std=1)
std_scaler = StandardScaler()
X_standardized = std_scaler.fit_transform(X)

# Step 3: Apply MinMaxScaler (Range [0, 1])
minmax_scaler = MinMaxScaler()
X_normalized = minmax_scaler.fit_transform(X)

print("\n--- STANDARDIZED FEATURES (StandardScaler: mu=0, sigma=1) ---")
print(pd.DataFrame(X_standardized, columns=X.columns).round(3).head(4))

print("\n--- NORMALIZED FEATURES (MinMaxScaler: [0, 1]) ---")
print(pd.DataFrame(X_normalized, columns=X.columns).round(3).head(4))

# Step 4: Partition dataset into Train (80%) and Test (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X_standardized, y, test_size=0.20, random_state=42, stratify=y
)

print(f"\n--- PARTITION SIZES ---")
print(f"Training Features Shape : {X_train.shape} | Training Labels: {len(y_train)}")
print(f"Testing Features Shape  : {X_test.shape}  | Testing Labels : {len(y_test)}")
