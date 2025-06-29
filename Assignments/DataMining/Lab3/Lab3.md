[[Lab]]

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from data
df = pd.read_csv('iris.csv')
df.info()

# View the top 5 entries
df.head()

df.tail()

# view some random samples
df.sample(3)

# check for missing values
df.isnull().sum()

# view the class distribution
class_labels = df['Species'].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(class_labels.index, class_labels.values)
plt.xlabel('Species')
plt.ylabel('Counts')
plt.title('Species Distribution')
plt.savefig('diagram1.png')
plt.show()

# Compute the boxplot
import seaborn as sns
sns.boxplot(data=df)

# Separate the data into X and y
X = df.drop(columns=['Species'])
y = df['Species']

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

acc_list = []
for k in range(1, 21):
	model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
	model = KNeighborsClassifier(n_neighbors=k)
	model.fit(X_train, y_train)
	y_preds = model.predict(X_test)
	acc_list.append(accuracy_score(y_test, y_preds))
acc_list
pplt.figure(figsize=(8, 6))
plt.bar(class_labels.index, class_labels.values)
plt.plot(range(1, 21), acc_list)
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.xticks(ticks=range(1, 21))
plt.title("k vs accuracy")
plt.savefig('pre.png')
plt.show()

model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=42))
model.fit(X_train, y_train)
y_preds = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, Y_preds)*100}")
print("\n", classification_report(y_text, y_preds))

cm = confusion_matric(y_test, y_preds)
cm_plot = ConfusionMatrixDisplay(
	confusion_matrix=cm, display_labels=df["Species"].unique()
)
cm_plot.plot()

import joblib

joblib.dump(model, "model.joblib")
```