import streamlit as st
from backend.pupil import detect_pupil
import tempfile
import sys
import os

sys.path.append(os.path.abspath("."))

# -------------------------------
# ✅ VALIDATION FUNCTION
# -------------------------------
def is_valid_pupil(data):
    if data is None:
        return False

    if data.get("pupil_area", 0) <= 0:
        return False

    if data.get("radius", 0) <= 0:
        return False

    if data.get("radius", 0) > 200:
        return False

    return True


# Page config
st.set_page_config(page_title="Smart Pupillometry", layout="centered")

# 🎨 STYLE
st.markdown("""
    <style>
        body { background-color: #0E1117; }

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
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🧠 Smart Pupillometry</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered eye triage system</div>', unsafe_allow_html=True)

# Upload
uploaded_file = st.file_uploader("📸 Upload an eye image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", width=300)

    if st.button("🔍 Analyze"):

        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.getvalue())
            temp_path = tmp.name

        # Run detection
        data = detect_pupil(temp_path)

        # -------------------------------
        # 🚨 VALIDATION STEP
        # -------------------------------
        if not is_valid_pupil(data):
            st.error("❌ No valid pupil detected. Please upload a clear eye image.")
            st.stop()

        # Check expected output structure
        required_keys = ["pupil_area", "radius", "normalized_radius", "status", "priority"]
        if not all(key in data for key in required_keys):
            st.error("⚠️ Invalid analysis result. Try another image.")
            st.stop()

        # -------------------------------
        # 📊 DISPLAY RESULTS
        # -------------------------------
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
            <div class="{priority_class.get(data['priority'], 'low')}">
                🚨 {data['priority']} PRIORITY
            </div>
        </div>
        """, unsafe_allow_html=True)
