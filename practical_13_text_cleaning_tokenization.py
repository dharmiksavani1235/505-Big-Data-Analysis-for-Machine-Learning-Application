"""
DS-505 Practical: Text Cleaning and Tokenization
Simple student-friendly program based on the uploaded workbook.
"""

import string

# Step 1: Raw noisy text string
raw_text = "   *** Big Data Handling & Machine Learning with Apache Spark, PySpark & LLMs! Are you Ready???   "

print("--- RAW TEXT INPUT ---")
print(f"'{raw_text}'")

# Step 2: Text Normalization (Lowercasing & Whitespace Stripping)
cleaned_text = raw_text.strip().lower()

# Step 3: Punctuation Removal using replace / string translation
punctuation_marks = string.punctuation
for char in punctuation_marks:
    cleaned_text = cleaned_text.replace(char, " ")

# Step 4: Normalize multiple spaces to single space
cleaned_text = " ".join(cleaned_text.split())

print("\n--- CLEANED & NORMALIZED TEXT ---")
print(f"'{cleaned_text}'")

# Step 5: Word Tokenization using split()
tokens = cleaned_text.split()

print("\n--- EXTRACTED WORD TOKENS ---")
print(f"Token Count : {len(tokens)}")
print(f"Tokens List : {tokens}")
