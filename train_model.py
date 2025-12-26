import pandas as pd
import numpy as np
import re
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def extract_features(password):
    length = len(password)
    upper = len(re.findall(r'[A-Z]', password))
    lower = len(re.findall(r'[a-z]', password))
    digits = len(re.findall(r'[0-9]', password))
    special = len(re.findall(r'[^A-Za-z0-9]', password))

    entropy = 0
    if length > 0:
        prob = 1 / length
        entropy = -length * prob * math.log2(prob)

    return [length, upper, lower, digits, special, entropy]

# Load dataset
df = pd.read_csv("dataset.csv")

X = np.array([extract_features(p) for p in df['password']])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("password_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
