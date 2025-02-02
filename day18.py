import numpy as np
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# Sample data
X = np.array([50, 120, 150, 75, 12, 14, 10]).reshape(-1, 1)
y = np.array([80, 150, 200, 100, 20, 25, 15])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Plot the results
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Linear regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()