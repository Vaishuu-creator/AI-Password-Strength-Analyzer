import re
import math
import pickle
import numpy as np

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

    return np.array([[length, upper, lower, digits, special, entropy]])

def suggestions(password):
    tips = []
    if len(password) < 8:
        tips.append("Increase password length to at least 8 characters")
    if not re.search(r'[A-Z]', password):
        tips.append("Add uppercase letters")
    if not re.search(r'[a-z]', password):
        tips.append("Add lowercase letters")
    if not re.search(r'[0-9]', password):
        tips.append("Include numbers")
    if not re.search(r'[^A-Za-z0-9]', password):
        tips.append("Add special characters")

    return tips

# Load trained model
with open("password_model.pkl", "rb") as f:
    model = pickle.load(f)

password = input("Enter your password: ")

features = extract_features(password)
prediction = model.predict(features)[0]

labels = {0: "WEAK", 1: "MEDIUM", 2: "STRONG"}

print("\nPassword Strength:", labels[prediction])

if prediction != 2:
    print("\nSuggestions to improve:")
    for tip in suggestions(password):
        print("-", tip)
else:
    print("Great! Your password is secure 🔐")
