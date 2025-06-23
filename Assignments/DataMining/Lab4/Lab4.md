```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bbc_news_dataset.csv")
print(df.info())

df.isnull().sum()

x = df["Text"]
y = df["Category"]

Category_names = df["Category"].unique()
print(Category_names)

import seaborn as sns
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="Category")
plt.xticks(rotation=45)
plt.title("News Categories Distribution")
plt.show()

from sklearn.model_selection import train_test_split X_train, X_test, y_train, y_test = train_test_split(
	x, y, test_size=0.2, random_state=42
)

from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (
	accuracy_score,
	classification_report,
	confusion_matrix,
	ConfusionMatrixDisplay
)
model = make_pipeline(TfidVectorizer(stop_words="english"), MultinomialNB())
model.fit(X_train, y_train)
y_preds = model.predict(X_test)
print(f"Accuracy is {accuracy_score(y_test, y_preds)*100}")
print("\n", classification_report(y_test, y_preds))

cm = confusion_matrix(y_test, y_preds)
cm_plot = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.category_names)
cm_plot.plot()
plt.xticks(rotation=45)
plt.title("Confusion Matric of News Category Classifier")
plt.show()

news = [
    "The latest football match ended in a draw, with great performances from both team"
    "The government announced new aid to Ukraine following catastrophic talks with"
]

news_preds = model.predict(news)
for text, prediction in zip(news, news_preds):
    print(f"Text = {text}\nPredicted Category = {prediction}")

import joblib

joblib.dump(model, "model.pkl")

```