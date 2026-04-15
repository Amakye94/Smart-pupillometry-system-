# 🧠 Smart Pupillometry Triage System

An AI-powered eye analysis system that detects pupil size from images and classifies triage priority.

---

## 🚀 Features

* 📸 Upload eye images
* 🔍 Detect pupil using OpenCV
* 📊 Calculate pupil size and radius
* 🚨 Classify triage priority (LOW / MEDIUM / HIGH)
* 📱 Works on mobile via Streamlit

---

## 🛠️ Tech Stack

* Python
* OpenCV
* Streamlit
* NumPy

---

## 📦 Installation

Clone the repository:

git clone https://github.com/Amakye94/Smart-pupillometry-system-.git
cd Smart-pupillometry-system-

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run App.py

---

## 🌍 Deployment

This project is deployed using Streamlit Community Cloud.

---

## ⚙️ Requirements

streamlit
opencv-python-headless==4.8.0.76
numpy<2

---

## 📊 How It Works

1. Upload an eye image
2. Image is converted to grayscale
3. Thresholding is applied
4. Largest contour (pupil) is detected
5. Radius and area are calculated
6. Triage level is assigned

---

##NB
This project is for educational purposes only.
Not for real medical diagnosis.

---

## 👨‍💻 Authors  Pupils Team Nexus

Ebenezer Asamoah Amakye, supported by Eric Jnr Ampah, Moses Oluwaseye moses.
