"""
DS-505 Practical: Decision Tree and KNN Classification
Simple student-friendly program based on the uploaded workbook.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1: Load standard Iris multiclass dataset
iris = load_iris()
X, y = iris.data, iris.target

# Step 2: Split into Train (70%) and Test (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

# Step 3: Train Decision Tree Classifier
dt_model = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)
dt_acc = accuracy_score(y_test, dt_preds)

# Step 4: Train K-Nearest Neighbors Classifier (K=5)
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_preds = knn_model.predict(X_test)
knn_acc = accuracy_score(y_test, knn_preds)

# Step 5: Compare Performance
print("--- MODEL EVALUATION & COMPARISON ---")
print(f"1. Decision Tree Accuracy : {dt_acc * 100:.2f}%")
print("Confusion Matrix (Decision Tree):")
print(confusion_matrix(y_test, dt_preds))

print(f"\n2. K-Nearest Neighbors Accuracy (K=5) : {knn_acc * 100:.2f}%")
print("Confusion Matrix (KNN):")
print(confusion_matrix(y_test, knn_preds))
