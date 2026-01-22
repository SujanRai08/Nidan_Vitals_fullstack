
---

### ** Backend README (`backend/README.md`)**

# Nidan Vitals Backend - FastAPI

This is the **backend** of the Nidan Vitals Fullstack project. It provides API endpoints for storing and retrieving patient vital records in FHIR format using **FastAPI**.

---

## Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Pydantic** (for data validation)
- **CORS Middleware** for frontend communication
- **Uvicorn** for running the ASGI server

---

## Features

- **GET /api/fhir/observation**: Fetch all observations or filter by patient ID / risk status
- **POST /api/fhir/observation**: Save new observation (height, weight, BP)
- Handles **BMI calculation** and categorizes risk automatically
- Returns data in **FHIR Observation JSON format**

---

## Getting Started

1. Clone the repository:
```bash
git clone <repo-url>
cd nidan_vitals_fullstack/backend
```


2. Install dependencies:
```bash
pip install -r requirements.txt
```

3.  Start the server:
```bash
uvicorn main:app --reload
```

4. API will be available at:
```
http://127.0.0.1:8000
```

## Folder Structure

```
backend/
|---- app/
      |---- models/
      |---- storage/
      |---- utils/
      |---- services/
      |---- controllers/
|---- test
|---- main.py
|---- .env
```


## Notes
Ensure CORS middleware allows requests from frontend (http://localhost:8000 by default)
Designed to work with frontend dashboard
Follow FHIR Observation format for storing patient vitals