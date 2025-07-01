import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(0)
num_samples = 1000

X = np.random.rand(num_samples, 5)  

true_coefficients = np.array([0.5, -0.2, 0.1, -0.3, 0.4])
logits = np.dot(X, true_coefficients)
probabilities = 1 / (1 + np.exp(-logits))
y = np.random.binomial(1, probabilities)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Classification Report:")
print(classification_report(y_test, y_pred))
