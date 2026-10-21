"""
DS-505 Practical: Memory Optimization using Dtype Downcasting
Simple student-friendly program based on the uploaded workbook.
"""

import pandas as pd
import numpy as np

# Step 1: Synthesize a 100,000-row dataset with unoptimized default types
np.random.seed(42)
n_rows = 100_000

df = pd.DataFrame({
    'User_ID': np.random.randint(1000, 9999, size=n_rows, dtype='int64'),
    'Age': np.random.randint(18, 70, size=n_rows, dtype='int64'),
    'Account_Balance': np.random.uniform(500.0, 50000.0, size=n_rows),
    'Subscription_Type': np.random.choice(['Basic', 'Standard', 'Premium', 'VIP'], size=n_rows),
    'Active_Status': np.random.choice(['Active', 'Inactive'], size=n_rows)
})

# Step 2: Measure baseline deep memory footprint
baseline_mem = df.memory_usage(deep=True).sum() / (1024 * 1024)
print("--- BASELINE MEMORY PROFILING ---")
print(df.dtypes)
print(f"Initial Memory Usage: {baseline_mem:.2f} MB")

# Step 3: Perform intelligent dtype optimization
df_opt = df.copy()

# Downcast integers
df_opt['User_ID'] = pd.to_numeric(df_opt['User_ID'], downcast='integer')
df_opt['Age'] = pd.to_numeric(df_opt['Age'], downcast='integer')

# Downcast floats
df_opt['Account_Balance'] = pd.to_numeric(df_opt['Account_Balance'], downcast='float')

# Convert repetitive object strings to category
df_opt['Subscription_Type'] = df_opt['Subscription_Type'].astype('category')
df_opt['Active_Status'] = df_opt['Active_Status'].astype('category')

# Step 4: Measure optimized memory usage
opt_mem = df_opt.memory_usage(deep=True).sum() / (1024 * 1024)
savings_pct = ((baseline_mem - opt_mem) / baseline_mem) * 100

print("\n--- OPTIMIZED MEMORY PROFILING ---")
print(df_opt.dtypes)
print(f"Optimized Memory Usage: {opt_mem:.2f} MB")
print(f"Memory Footprint Reduction: {savings_pct:.2f}% RAM Saved!")
