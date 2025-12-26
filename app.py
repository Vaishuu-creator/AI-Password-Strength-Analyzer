import streamlit as st
import re
import math
import pickle
import numpy as np

# ---------------- Load Model ----------------
with open("password_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- Feature Extraction ----------------
def extract_features(password):
    length = len(password)
    upper = len(re.findall(r'[A-Z]', password))
    lower = len(re.findall(r'[a-z]', password))
    digits = len(re.findall(r'[0-9]', password))
    special = len(re.findall(r'[^A-Za-z0-9]', password))

    entropy = 0
    if length > 0:
        p = 1 / length
        entropy = -length * p * math.log2(p)

    return np.array([[length, upper, lower, digits, special, entropy]])

# ---------------- Rule Check ----------------
def password_rules(password):
    return {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letter (A-Z)": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter (a-z)": bool(re.search(r"[a-z]", password)),
        "Number (0-9)": bool(re.search(r"[0-9]", password)),
        "Special character (!@#$)": bool(re.search(r"[^A-Za-z0-9]", password))
    }

# ---------------- UI ----------------
st.set_page_config(page_title="AI Password Strength Analyzer", page_icon="🔐")

st.title("🔐 AI Password Strength Analyzer")
st.markdown("### Secure your digital identity using AI")

password = st.text_input("Enter your password", type="password")

if password:
    features = extract_features(password)
    prediction = model.predict(features)[0]

    labels = {0: "WEAK", 1: "MEDIUM", 2: "STRONG"}
    colors = {0: "red", 1: "orange", 2: "green"}
    progress = {0: 0.3, 1: 0.65, 2: 1.0}

    # Strength Badge
    st.markdown(
        f"## Strength: <span style='color:{colors[prediction]}'>{labels[prediction]}</span>",
        unsafe_allow_html=True
    )

    # Progress Bar
    st.progress(progress[prediction])

    col1, col2 = st.columns(2)

    # ---------------- Left Column ----------------
    with col1:
        st.subheader("🔍 Rule Checklist")
        rules = password_rules(password)
        for rule, passed in rules.items():
            if passed:
                st.success(f"✔ {rule}")
            else:
                st.error(f"❌ {rule}")

    # ---------------- Right Column ----------------
    with col2:
        st.subheader("📊 Password Insights")
        st.write(f"**Length:** {len(password)}")
        st.write(f"**Entropy Score:** {round(features[0][-1], 2)}")

        if prediction != 2:
            st.warning("⚠️ Suggestions to Improve")
            for rule, passed in rules.items():
                if not passed:
                    st.write("• " + rule)
        else:
            st.success("✅ Excellent! Your password is highly secure.")

st.markdown("---")
st.caption("Python • ML • Streamlit")
