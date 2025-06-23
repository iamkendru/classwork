
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 df = pdf.read_csv('iris.csv')
print(df.info)
df.head()
df.tail()
df.sample(3)
df.isnull().sum()
class_labels = df['Specoes'].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(class_labels.index, class_labels.values)
plt.xlabel('Species')
plt.ylabel('Counts')
plt.title('Species Distribution')
plt.show()

import seaborn as sns
sns.boxplot(data=df)

X = df.drop(columns=['Species'])
y = df['Species']

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matric, ConfusionMatrixDisplay

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for k in range(1, 21):
	acc_list = []
	model = make_pipeline(StandardScaler[], KNeighborsClassifier(n_neighbors=k))
model.fit(X_train, y_train)
y_preds = model.predict(X_test)
acc_list.append(accuracy_score(y_test, y_preds))
plt.figure(figsize=(8, 6))
plt.plot(range(1, 21), acc_list)
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.xticks(ticks=range(1, 21))
plt.title('k vs accuracy')

plt.show()

model = mkae_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=42))
model.fit(X_train, y_train)
y_preds = model.predict(X_test)
print(f'Accuracy: (accuracy_score(y_test, y_preds)*100)')
print("\n", classification_report(y_test, y_pred))

cm = confusion_matric(y_test, y_preds)
cm_plot = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=df['Species'].unique())
cm_plot.plot()
```
