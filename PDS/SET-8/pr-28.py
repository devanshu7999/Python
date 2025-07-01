import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(0)
num_samples = 1000

X = np.random.rand(num_samples, 5) 

true_coefficients = np.array([50000, 20000, 30000, 1000, -5000])
noise = np.random.normal(0, 10000, num_samples)
y = np.dot(X, true_coefficients) + noise

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
