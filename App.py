import streamlit as st
from backend.pupil import detect_pupil
import tempfile
import sys
import os
sys.path.append(os.path.abspath("."))

# Page config
st.set_page_config(page_title="Smart Pupillometry", layout="centered")

# 🎨 STYLE
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
        }

        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #4FC3F7;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #BBBBBB;
            margin-bottom: 20px;
        }

        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #1E1E1E;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
            color: white;
        }

        .high {
            background-color: #ff4d4d;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 18px;
        }

        .medium {
            background-color: #ffa500;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 18px;
        }

        .low {
            background-color: #2ecc71;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 18px;
        }

        .btn {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🧠 Smart Pupillometry</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered eye triage system</div>', unsafe_allow_html=True)

# Upload
uploaded_file = st.file_uploader("📸 Upload an eye image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", width=300)

    # 🔥 ANALYZE BUTTON (IMPORTANT UX FIX)
    if st.button("🔍 Analyze"):
        
        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.getvalue())
            temp_path = tmp.name

        # 🔥 DIRECT CALL (NO BACKEND)
        data = detect_pupil(temp_path)

        st.write("")
        st.markdown("### 📊 Analysis Result")

        priority_class = {
            "HIGH": "high",
            "MEDIUM": "medium",
            "LOW": "low"
        }

        st.markdown(f"""
        <div class="card">
            <p><b>Pupil Area:</b> {data['pupil_area']}</p>
            <p><b>Radius:</b> {data['radius']}</p>
            <p><b>Normalized Size:</b> {data['normalized_radius']}</p>
            <p><b>Status:</b> {data['status']}</p>
            <br>
            <div class="{priority_class[data['priority']]}">
                🚨 {data['priority']} PRIORITY
            </div>
        </div>
        """, unsafe_allow_html=True)
        def safe_predict(model, features):
    try:
        # Get probabilities
        probs = model.predict_proba([features])[0]
        confidence = max(probs)

        # 🔹 Confidence threshold (tune this: 0.6–0.8)
        if confidence < 0.7:
            return "Invalid input (low confidence)", confidence

        # 🔹 Normal prediction
        prediction = model.predict([features])[0]
        return prediction, confidence

    except Exception as e:
        return "Invalid input (error in processing)", 0
