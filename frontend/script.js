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
// cateogrory badge
function getCategoryBadge(cat) {
    if (cat === "Obese") return "bg-danger";
    if (cat === "Overweight") return "bg-warning text-dark";
    if (cat === "Normal") return "bg-success";
    return "bg-info";
}

// Fetch and Display Table Data
async function loadObservations(patientId = "", risk = "All") {
    let url = `${API_BASE_URL}?risk=${risk}`;
    if (patientId) url += `&patientId=${patientId}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        const tableBody = document.getElementById('vitalsTableBody');
        tableBody.innerHTML = "";

        data.forEach(obs => {
            // Find height and weight values from FHIR components
            const height = obs.component.find(
                c => c.code.coding[0].code === "8302-2"
            )?.valueQuantity.value || "--";
            const weight = obs.component.find(
                c => c.code.coding[0].code === "29463-7"
            )?.valueQuantity.value || "--";
            
            const row = `
                <tr>
                    <td>${obs.subject.reference}</td>
                    <td>${weight}kg / ${height}cm</td>
                    <td><span class="badge ${getCategoryBadge(obs.bmi_category)}">${obs.bmi_category}</span></td>
                    <td><strong>${obs.risk_status}</strong></td>
                    <td>${new Date(obs.effectiveDateTime).toLocaleString()}</td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });
    } catch (error) {
        console.error("Error loading data:", error);
    }
}

// Save Observation (POST)
async function saveObservation() {
    const payload = {
        resourceType: "Observation",
        subject: { reference: document.getElementById('patientId').value },
        component: [
            {
                code: { coding: [{ code: "8302-2", display: "Height" }] },
                valueQuantity: { value: parseFloat(document.getElementById('height').value), unit: "cm" }
            },
            {
                code: { coding: [{ code: "29463-7", display: "Weight" }] },
                valueQuantity: { value: parseFloat(document.getElementById('weight').value), unit: "kg" }
            },
            {
                code: { coding: [{ code: "8480-6", display: "Systolic BP" }] },
                valueQuantity: { value: parseFloat(document.getElementById('systolic').value), unit: "mmHg" }
            },
            {
                code: { coding: [{ code: "8462-4", display: "Diastolic BP" }] },
                valueQuantity: { value: parseFloat(document.getElementById('diastolic').value), unit: "mmHg" }
            }
        ]
    };

    const response = await fetch(API_BASE_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    if (response.ok) {
        alert("Record Saved Successfully!");
        loadObservations(); // Refresh table
    }
}

// Event Listeners
document.getElementById('height').addEventListener('input', calculateLiveBMI);
document.getElementById('weight').addEventListener('input', calculateLiveBMI);
document.getElementById('saveBtn').addEventListener('click', saveObservation);
document.getElementById('searchBar').addEventListener('input', (e) => loadObservations(e.target.value));

document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        loadObservations("", e.target.getAttribute('data-risk'));
    });
});

loadObservations();