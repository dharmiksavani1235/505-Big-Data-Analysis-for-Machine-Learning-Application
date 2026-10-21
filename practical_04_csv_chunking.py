"""
DS-505 Practical: Batch CSV Processing using Chunking
Simple student-friendly program based on the uploaded workbook.
"""

import pandas as pd
import numpy as np

# Step 1: Generate a sample CSV file on disk with 5,000 transaction records
csv_filename = "transactions_stream.csv"
records = 5000

df_temp = pd.DataFrame({
    'Txn_ID': range(1, records + 1),
    'Amount': np.random.uniform(10.0, 500.0, size=records).round(2),
    'Category': np.random.choice(['Retail', 'Dining', 'Travel', 'Utilities'], size=records)
})
df_temp.to_csv(csv_filename, index=False)
print(f"Created '{csv_filename}' with {records:,} records.")

# Step 2: Process the CSV file in chunks to avoid high RAM consumption
chunk_size = 1000
total_records = 0
running_sum = 0.0
chunk_number = 1

print(f"\n--- PROCESSING IN CHUNKS OF {chunk_size} ROWS ---")
for chunk in pd.read_csv(csv_filename, chunksize=chunk_size):
    chunk_count = len(chunk)
    chunk_sum = chunk['Amount'].sum()
    
    total_records += chunk_count
    running_sum += chunk_sum
    
    print(f"Chunk {chunk_number}: Processed {chunk_count} rows | Chunk Sum: ${chunk_sum:,.2f} | Running Total: ${running_sum:,.2f}")
    chunk_number += 1

overall_average = running_sum / total_records
print("\n--- FINAL AGGREGATION METRICS ---")
print(f"Total Records Processed : {total_records:,}")
print(f"Total Cumulative Volume : ${running_sum:,.2f}")
print(f"Overall Average Value   : ${overall_average:.2f}")
