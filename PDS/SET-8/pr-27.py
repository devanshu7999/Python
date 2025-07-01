import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("Coefficients: ", model.coef_)

print("Intercept: ", model.intercept_)
