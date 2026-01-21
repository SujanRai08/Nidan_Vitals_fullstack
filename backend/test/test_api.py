from fastapi.testclient import TestClient
from main import app 
from app.storage.db import db
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    db.clear()

def test_create_and_get_observation():
    # 1. Define a Valid FHIR Payload
    sample_payload = {
        "resourceType": "Observation",
        "subject": { "reference": "Patient/P-999" },
        "component": [
            {
                "code": { "coding": [{ "code": "8302-2", "display": "Height" }] },
                "valueQuantity": { "value": 180, "unit": "cm" }
            },
            {
                "code": { "coding": [{ "code": "29463-7", "display": "Weight" }] },
                "valueQuantity": { "value": 95, "unit": "kg" }
            }
        ]
    }

    # 2. Test POST (Create)
    post_response = client.post("/api/fhir/observation", json=sample_payload)
    assert post_response.status_code == 200
    
    post_data = post_response.json()
    assert post_data["status"] == "success"
    # BMI calculation: 95 / (1.8^2) = 29.32 (Overweight)
    assert post_data["category"] == "Overweight"

    # 3. Test GET (Retrieve All)
    get_response = client.get("/api/fhir/observation")
    assert get_response.status_code == 200
    all_data = get_response.json()
    assert len(all_data) >= 1

    # 4. Test Search Filter (Patient ID)
    # We use query parameters ?patientId=P-999
    search_response = client.get("/api/fhir/observation?patientId=P-999")
    assert search_response.status_code == 200
    search_results = search_response.json()
    
    # Check if the search actually returned our patient
    assert len(search_results) > 0
    assert "P-999" in search_results[0]["subject"]["reference"]

    # 5. Test Risk Filter
    filter_response = client.get("/api/fhir/observation?risk=Overweight")
    assert filter_response.status_code == 200
    for record in filter_response.json():
        assert record["bmi_category"] == "Overweight"

def test_invalid_resource_type():
    # Test error handling for wrong FHIR resource types
    bad_payload = {"resourceType": "Patient"}
    response = client.post("/api/fhir/observation", json=bad_payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid FHIR resources"