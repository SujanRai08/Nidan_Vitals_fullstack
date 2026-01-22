# Nidan Vitals Dashboard - Frontend

This is the **frontend** of the Nidan Vitals Fullstack project. It provides a dashboard interface for entering and viewing patient vitals using HTML, Bootstrap, and JavaScript.

---

## Tech Stack

- **HTML5**
- **Bootstrap 5**
- **JavaScript (Vanilla)**
- **Fetch API** (to interact with the FastAPI backend)

---

## Features

- **Live BMI Calculation**: Automatically calculates BMI based on height and weight input.
- **Patient Vitals Entry**: Form to submit height, weight, and blood pressure readings.
- **Vitals Table**: Displays patient records dynamically with filtering by risk category.
- **Search Functionality**: Search patients by their ID.
- **Risk Badge Colors**: Normal (green), Overweight (yellow), Obese (red), Underweight (blue).

---

## Getting Started

1. Clone the repository:
```bash
git clone <repo-url>
cd nidan_vitals_fullstack/frontend
```

2. open index.html in your browser and go live

3. Make sure the backend FASTAPI server is running at:
```bash
http://127.0.0.1:8000/api/fhir/observation
```

4. Start interacting with the dashboard:
Enter vitals and see live BMI updates
Save records and see them in the table

## Folder Structure

```
frontend/
|---- index.html
|---- script.js
|---- README.md
```

## Notes
Designed to work with FastAPI backend
Fully responsive using Bootstrap
No external JS frameworks required