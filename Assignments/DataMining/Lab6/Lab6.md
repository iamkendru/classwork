# Class
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

# Assignment(Regression)

```python
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
data = fetch_openml(name="house_prices", version=1, as_frame=True)
df = data.frame

# preprocess
df = df.select_dtypes(include=["number"]).dropna()

# Define features and targets
X = df.drop(columns=["SalePrice"])
y = df["SalePrice"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normalize
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train MLP Regressor
model = MLPRegressor(
    hidden_layer_sizes=(100, 50),
    max_iter=1000,
    random_state=42,
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print results
print("Evaluation Metrics:")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R² Score: {r2:.4f}")

# Actual vs Predicted
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
plt.xlabel("Actual Sale Price")
plt.ylabel("Predicted Sale Price")
plt.title("Actual vs Predicted Sale price")
plt.grid(True)
plt.tight_layout()
plt.show()

# Residuals plot
residuals = y_test - y_pred

plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, bins=30)
plt.xlabel("Residuals (Actual - Predicted)")
plt.grid(True)
plt.tight_layout()
plt.show()

```