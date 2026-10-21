"""
DS-505 Practical: Vocabulary Frequency and Stopword Filtering
Simple student-friendly program based on the uploaded workbook.
"""

from collections import Counter

# Step 1: Text Corpus
corpus = """
Big data refers to massive volumes of structured and unstructured data.
Apache Spark is a distributed computing system designed for big data processing.
Machine learning models learn patterns from large scale big data.
Natural language processing and transformers enable intelligent understanding of text data.
"""

# Step 2: Define basic English stop words list
stopwords = {'to', 'of', 'and', 'a', 'is', 'for', 'from', 'in'}

# Step 3: Clean and tokenize corpus
words = corpus.lower().replace('.', '').replace(',', '').split()

# Step 4: Filter out stop words
filtered_words = [w for w in words if w not in stopwords]

# Step 5: Count word frequencies
frequency_counter = Counter(filtered_words)

print("--- VOCABULARY FREQUENCY ANALYSIS ---")
print(f"Total Raw Words         : {len(words)}")
print(f"After Stopword Removal  : {len(filtered_words)}")
print(f"Total Unique Vocabulary : {len(frequency_counter)}")

print("\n--- TOP 5 MOST FREQUENT KEYWORDS ---")
for word, freq in frequency_counter.most_common(5):
    print(f"Keyword: {word:<15} | Frequency: {freq}")
