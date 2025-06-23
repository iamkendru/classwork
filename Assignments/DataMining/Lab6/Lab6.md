```python

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
 X = np.arange(0, 1, 0.02)
y = 0.77 * X + 0.33
 print(f"{X[:10]} \n {y[:10]}")
print(f"Shape of X = {X.shape}")
print(f"Shape of y = {y.shape}")
 split = int(len(X) * 0.8)
X_train, y_train = X[:split], y[:split]
X_test, y_test = X[split:], y[split:]
  def plot_data(
X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test,
predictions=None
):
plt.figure(figsize=(8, 6))
plt.scatter(X_train, y_train, c="blue", label="Training Data")
plt.scatter(X_test, y_test, c="red", label="Testing Data")
if predictions is not None:
plt.scatter(X_test, predictions, c="green", label="Predicted
Data")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Scatter Plot of Data")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
  plot_data()

```