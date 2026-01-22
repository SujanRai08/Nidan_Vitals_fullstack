const API_BASE_URL = "http://127.0.0.1:8000/api/fhir/observation";

// Live BMI Calculation
function calculateLiveBMI() {
    const h = document.getElementById('height').value;
    const w = document.getElementById('weight').value;
    const display = document.getElementById('bmiDisplay');

    if (h > 0 && w > 0) {
        const bmi = (w / ((h / 100) ** 2)).toFixed(2);
        let status = "Normal";
        let color = "bg-success text-white";

        if (bmi < 18.5) { status = "Underweight"; color = "bg-info"; }
        else if (bmi >= 25 && bmi < 30) { status = "Overweight"; color = "bg-warning"; }
        else if (bmi >= 30) { status = "Obese"; color = "bg-danger text-white"; }

        display.innerHTML = `BMI: ${bmi} (${status})`;
        display.className = `fw-bold p-2 rounded bmi-badge text-center ${color}`;
    } else {
        display.innerHTML = "BMI: -- (Enter Height & Weight)";
        display.className = "fw-bold p-2 rounded bmi-badge text-center border";
    }
}
// fetch and display from table