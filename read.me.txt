# 🛡️ Cyber Guard Pro

## 📌 Overview

Cyber Guard Pro is a security-focused web application that helps users evaluate password strength, detect compromised credentials, and scan URLs for potential threats using real-world cybersecurity APIs. The application also includes user authentication and activity tracking.

---

## 🚀 Features

### 🔐 Password Auditor

* Checks password strength (Weak / Medium / Strong)
* Detects if a password has been leaked using a k-anonymity model (Have I Been Pwned API)

### 🌐 URL Scanner

* Scans URLs using VirusTotal API
* Displays analysis results (malicious vs harmless)

### 🔑 Password Generator

* Generates strong, random passwords using Python’s secure `secrets` module

### 📊 Dashboard & History

* User login system
* Stores and displays recent activity

---

## 🛠️ Tech Stack

* Python
* Streamlit
* REST APIs
* VirusTotal API
* Have I Been Pwned API (k-anonymity approach)

---

## ⚙️ How It Works

1. User logs into the application
2. Inputs a password or URL
3. Application sends requests to external APIs
4. Displays security results and insights

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/cyber-guard-pro.git
cd cyber-guard-pro
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔒 Environment Setup

Create a `.env` file in the root directory and add:

```
VT_API_KEY=your_virustotal_api_key
```

Make sure your API keys are **not exposed** in the repository.

---

## 📁 Project Structure

```
cyber-guard-pro/
│
├── app.py          # Main Streamlit application
├── api.py          # External API integrations
├── utils.py        # Password logic and utilities
├── db.py           # Database and user management
├── requirements.txt
└── README.md
```

---

## 🚧 Future Improvements

* Add frontend UI (React or similar)
* Improve VirusTotal polling and response handling
* Enhance authentication and security features

---

## 👨‍💻 Author

Joel Chinta

---

## ⭐ Note

This project is built for learning and demonstration purposes, focusing on API integration and basic cybersecurity practices.
