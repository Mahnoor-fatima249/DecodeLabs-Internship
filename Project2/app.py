import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

# 1. Dataset loading (Iris flower data)
iris = load_iris()
X = iris.data
y = iris.target

# 2. Training aur Testing data ko split karna (80/20 ratio)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10  # random_state change kar di for uniqueness
)

# 3. Scaling (The Gatekeeper Rule)
iris_scaler = StandardScaler()
X_train = iris_scaler.fit_transform(X_train)
X_test = iris_scaler.transform(X_test)

# 4. KNN Model setup (Using flower_classifier name)
flower_classifier = KNeighborsClassifier(n_neighbors=5)
flower_classifier.fit(X_train, y_train)

# 5. Model prediction aur results
final_preds = flower_classifier.predict(X_test)

# 6. Evaluation metrics calculate karna
final_acc = accuracy_score(y_test, final_preds)
conf_matrix = confusion_matrix(y_test, final_preds)
f1 = f1_score(y_test, final_preds, average='weighted')

print(f"Accuracy: {final_acc}")
print("Confusion Matrix:\n", conf_matrix)
print(f"F1 Score: {f1}")

# 7. Visualization (Graph)
plt.bar(['KNN Performance'], [final_acc], color='blue')
plt.text(0, final_acc + 0.02, str(round(final_acc, 2)), ha='center')
plt.ylim(0, 1.1)
plt.title("DecodeLabs Project 2: Classification Result")
plt.show()
plt.savefig("my_knn_result.png")
