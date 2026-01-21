from app.services.observation_service import ObservationService

def test_bmi_calculation():
    bmi = ObservationService.calculate_bmi(70, 170)
    assert bmi == 24.22

def test_bmi_categories():
    assert ObservationService.bmi_category(17.0) == "Underweight"
    assert ObservationService.bmi_category(22.0) == "Normal"
    assert ObservationService.bmi_category(27.0) == "Overweight"
    assert ObservationService.bmi_category(35.0) == "Obese"

def test_risk_status_logic():
    assert ObservationService.get_risk_status(32.0, 120, 80) == "High Risk"

    assert ObservationService.get_risk_status(22.0, 145, 80) == "High Risk"

    assert ObservationService.get_risk_status(27.0, 120, 80) == "Warning"

    assert ObservationService.get_risk_status(22.0, 110, 70) == "Normal"