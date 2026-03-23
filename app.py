import streamlit as st
import pickle

from src.preprocessing import preprocess

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Financial Institution Phishing Detection System",
    page_icon="🔐",
    layout="centered"
)

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# =========================
# CUSTOM STYLING (CSS)
# =========================
st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #1f77b4;
}
.subtitle {
    font-size: 18px;
    color: gray;
    margin-bottom: 20px;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}
.phishing {
    background-color: #ffcccc;
    color: #990000;
}
.legit {
    background-color: #ccffcc;
    color: #006600;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="big-title">🔐 Financial Institution Phishing Email Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered financial email security system</div>', unsafe_allow_html=True)

# =========================
# INPUT BOX
# =========================
email_input = st.text_area("📧 Enter email text:", height=150)

# =========================
# BUTTON ACTION
# =========================
if st.button("🔍 Analyze Email"):

    if len(email_input.strip()) < 20:
        st.warning("⚠️ Please enter a complete email (at least 20 characters)")

    else:
        # Word count
        word_count = len(email_input.split())
        st.info(f"📊 Word count: {word_count}")

        # Preprocess
        clean_text = preprocess(email_input)
        vector = vectorizer.transform([clean_text])

        # Prediction
        prediction = model.predict(vector)[0]
        score = model.decision_function(vector)[0]

        # =========================
        # CONFIDENCE BAR
        # =========================
        confidence = min(max(abs(score) / 3, 0), 1)  # normalize
        st.progress(confidence)

        st.write(f"🔎 Confidence score: {round(score, 2)}")

        # =========================
        # EXPLANATION (KEYWORDS)
        # =========================
        phishing_keywords = [
            "urgent", "verify", "account", "login", "click", 
            "password", "bank", "suspend", "limited", "confirm"
        ]

        found_keywords = [word for word in phishing_keywords if word in email_input.lower()]

        if found_keywords:
            st.warning(f"⚠️ Suspicious keywords detected: {', '.join(found_keywords)}")

        # =========================
        # RESULT DISPLAY
        # =========================
        if prediction == 1:
            st.markdown(
                '<div class="result-box phishing">⚠️ Phishing Email Detected</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-box legit">✅ Legitimate Email</div>',
                unsafe_allow_html=True
            )