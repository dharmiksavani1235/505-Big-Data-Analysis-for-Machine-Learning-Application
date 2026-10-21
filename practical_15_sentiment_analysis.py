"""
DS-505 Practical: Sentiment Analysis using Hugging Face
Simple student-friendly program based on the uploaded workbook.
"""

from transformers import pipeline

# Step 1: Initialize pretrained Hugging Face Sentiment Analysis Pipeline
print("Loading Hugging Face sentiment-analysis pipeline...")
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Step 2: Define sample product & service customer reviews
reviews = [
    "PySpark makes distributed computing on massive datasets incredibly fast and enjoyable!",
    "The dataset had too many corrupted records and missing values, causing the training to crash.",
    "Transformers and Large Language Models are revolutionizing artificial intelligence.",
    "The data engineering pipeline was slow and poorly documented."
]

# Step 3: Run inference and display results
print("\n--- PREDICTED SENTIMENT SCORES ---")
for i, review in enumerate(reviews, 1):
    result = classifier(review)[0]
    label = result['label']
    score = result['score'] * 100
    print(f"Review {i}: '{review}'")
    print(f"Result   : [{label}] with {score:.2f}% confidence\n")
