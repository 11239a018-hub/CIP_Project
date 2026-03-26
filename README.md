# Virtual Vita – AI Healthcare Assistant

Virtual Vita is a full-stack AI-powered healthcare assistant that predicts possible diseases based on user-selected symptoms. It combines Machine Learning, a FastAPI backend, and an interactive frontend UI.

---

## Features

* Disease prediction using Machine Learning (Random Forest)
* FastAPI backend for real-time predictions
* Interactive frontend (HTML, JavaScript, CSS)
* Symptom-based input system
* End-to-end ML pipeline integration

---

## Project Structure

```
virtual-vita/
│
├── backend/              # FastAPI backend
│   ├── services/         # Prediction logic
│   ├── app.py            # API entry point
│
├── frontend/             # UI
│   ├── index.html
│   ├── chat.js
│   ├── style.css
│
├── training/             # Model training scripts
├── model_weights/        # (ignored in Git)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation & Setup

### Clone the repository

```
git clone https://github.com/<your-username>/virtual-vita.git
cd virtual-vita
```

---

### Create virtual environment

```
python -m venv vita_env
vita_env\Scripts\activate   # Windows
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

### Run backend

```
uvicorn backend.app:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

---

### Run frontend

Open:

```
frontend/index.html
```

(or use Live Server)

---

## API Endpoint

### POST `/predict`

**Request:**

```json
{
  "symptoms": ["fever", "headache"]
}
```

**Response:**

```json
{
  "disease": "Predicted Disease",
  "doctor": "Recommended Specialist",
  "risk_level": "Low/Medium/High",
  "treatment": "Basic guidance"
}
```

---

## Model Details

* Algorithm: Random Forest Classifier
* Input: Symptoms (multi-label encoding)
* Output: Disease prediction

---

## Model Performance

* Model: Random Forest Classifier
* Dataset: Symptom-based disease dataset
* Status: Initial prototype (evaluation in progress)

> Note: Model evaluation metrics (accuracy, precision, recall) will be added after further tuning and validation.

---

## Current Limitations

* Model accuracy is currently low due to limited dataset
* Class imbalance affects predictions
* Same disease prediction issue under improvement

---

## Future Improvements

* NLP-based symptom input (free text)
* Multilingual support (Telugu/Tamil/English)
* Improved ML model & dataset balancing
* Deployment (AWS / GCP / Render)
* Chatbot-style conversational UI

---

## Author

**Sushma Hiranya Indrakanti**
