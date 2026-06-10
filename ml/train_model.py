import pandas as pd
import pickle

from sklearn.feature_extraction.text import (
    CountVectorizer
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.preprocessing import (
    LabelEncoder
)

data = pd.read_csv(
    "ml/career_dataset.csv"
)

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(
    data["skills"]
)

encoder = LabelEncoder()

y = encoder.fit_transform(
    data["career"]
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

pickle.dump(
    model,
    open(
        "ml/career_model.pkl",
        "wb"
    )
)

pickle.dump(
    vectorizer,
    open(
        "ml/vectorizer.pkl",
        "wb"
    )
)

pickle.dump(
    encoder,
    open(
        "ml/encoder.pkl",
        "wb"
    )
)

print(
    "Career Model Trained Successfully"
)