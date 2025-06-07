# 🔍 Scam Detector - Flask App

This is a simple **AI-powered Flask web app** that detects potentially scam or fraudulent messages using keyword detection logic.  
It is designed to simulate how an early-stage scam filter could work — built for educational and demonstration purposes.

---

## 🚀 Features

- Detects scammy words like *"urgent"*, *"OTP"*, *"bank"*, *"verify"*, etc.
- Simple and clean Flask web interface
- Keyword-based flagging system
- Easy to run on local machine
- Educational prototype with real-world use case

---

## 🛠️ Tech Stack

- 🐍 Python (Flask)
- 🖼️ HTML Templates (Jinja2)
- 🧠 Basic NLP/Keyword Logic
- 🌐 Local Web Deployment

---

## 🧠 How it Works

1. User enters a message into the input box.
2. App scans message for suspicious keywords.
3. If scam-related keywords are detected → returns **"Scam Detected"**.
4. Else → returns **"Safe Message"**.

---

## 💻 How to Run Locally

```bash
git clone https://github.com/Jyoti678/Scam_detector.git
cd Scam_detector
pip install flask
python app.py
Then open your browser and go to:
👉 http://127.0.0.1:5000

📁 Project Structure
cpp
Copy
Edit
Scam_detector/
├── app.py
├── templates/
│   └── index.html
├── static/         # (optional: for CSS, JS, images)
└── README.md
📈 Future Scope
Add voice alert system

Train machine learning model for better detection

Multilingual keyword detection (regional scam messages)

Store message history for user review

Android app interface

🧑‍💻 Developed By
    Jyoti Airey
🎓 BCA Student | 🔒 Aspiring Cybersecurity Engineer | 💻 Python + Web Dev Enthusiast
🔗 GitHub: @Jyoti678
🎯 Goal: Crack Google Internship | Build Real-world Impact Projects


