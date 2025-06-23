[[Lab]]

# 1
```python
import numpy as np
import matplotlib.pyplot as plt

w = np.random.randn()
print(w)

x = 1.5
y = 0.5

epoch = 20
alpha = 0.1
errorList = []
for i in range(epoch):
	y_preds = x * w
	error = (y - y_preds) ** 2
	deltaW = -2 * (y - y_preds) * x
	w = w - deltaW * alpha
	errorList.append(error)
	print(f"Epoch{i+1}|Loss{error:.4f}")
 y_preds = x * w
print(y_preds)
 plt.figure(figsize=(8, 6))
plt.plot(range(epoch), errorList)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(ticks=range(epoch))
plt.title("EPOCHS VS LOSS")
plt.grid(True)
plt.show()

```

# 2
```python

import numpy as np
import matplotlib.pyplot as plt
 # Initialize weights and bias
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()
 x1 = 1.5
x2 = 1
y = 5
 epoch = 20
alpha = 0.1
errorlist = []
 for i in range(epoch):
# Forward pass
y_pred = x1 * w1 + x2 * w2 + b
  # Compute loss
error = (y - y_pred) ** 2
  # Compute gradients
deltaW1 = -2 * (y - y_pred) * x1
deltaW2 = -2 * (y - y_pred) * x2
deltaB = -2 * (y - y_pred)
  # Update weights and bias
w1 = w1 - deltaW1 * alpha
w2 = w2 - deltaW2 * alpha
b = b - deltaB * alpha
  # Record loss
errorlist.append(error)
  print(f"Epoch {i+1} | Loss: {error:.4f}")
 # Final prediction
y_pred = x1 * w1 + x2 * w2 + b
print("Final prediction:", y_pred)
# Plotting
plt.figure(figsize=(8, 6))
plt.plot(range(epoch), errorlist)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(ticks=range(epoch))
plt.title("EPOCHS vs LOSS")
plt.grid(True)
plt.show()

```

# 3

```python

import numpy as np
import matplotlib.pyplot as plt
 # Random initialization
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()
 # Inputs and target
x1 = 0.9
x2 = -16.5
y = 18.3
 epoch = 20
alpha = 0.1
errorlist = []
 for i in range(epoch):
# Forward pass
y_pred = x1 * w1 + x2 * w2 + b
  # Compute loss
error = (y - y_pred) ** 2
  # Compute gradients
deltaW1 = -2 * (y - y_pred) * x1
deltaW2 = -2 * (y - y_pred) * x2
deltaB = -2 * (y - y_pred)
  # Update parameters
w1 = w1 - deltaW1 * alpha
w2 = w2 - deltaW2 * alpha
b = b - deltaB * alpha
  errorlist.append(error)
print(f"Epoch {i+1} | Loss: {error:.4f}")
 # Final prediction
y_pred = x1 * w1 + x2 * w2 + b
print("\nFinal prediction:", y_pred)
 # Plotting lossplt.figure(figsize=(8, 6))
plt.plot(range(epoch), errorlist, marker='o')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.xticks(ticks=range(epoch))
plt.title("EPOCHS vs LOSS")
plt.grid(True)
plt.show()

```