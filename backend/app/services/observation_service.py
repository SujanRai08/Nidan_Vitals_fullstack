class ObservationService:

    @staticmethod
    def calculate_bmi(weight_kg,height_cm):
        "Convert cm to meters because the BMI formula is kg/m^2"
        height_m = height_cm/100
        return round(weight_kg/(height_m ** 2),2)
    
    @staticmethod
    def bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        return "Obese"
    
    @staticmethod
    def get_risk_status(bmi,systolic, diastolic):
        """
        Requirement: Red Alerts if BMI >= 30 or BP >= 140/90.
        Returns: 'High Risk', 'Warning', or 'Normal'
        """
        if bmi >= 30 or systolic >= 140 or diastolic >= 90:
            return "High Risk"  # Red
        elif 25 <= bmi < 30:
            return "Warning"    # Orange
        return "Normal" # Green
    
    @staticmethod 
    def create_fhir_payload(obs_obj):
        """
        Python class into the specific json format required by the FHIR R4 standard.
        """
        fhir_data = {
            "resourceType": "Observation",
            "status": "final",
            "code": {
                "coding": [{"system": "http://loinc.org", "code": "85353-1", "display": "Vital signs panel"}]
            },
            "subject": {"reference": f"Patient/{obs_obj.patient_id}"},
            "effectiveDateTime": obs_obj.effective_datetime,
            "component": [
            ] # add or look every componenets 
        }

        for key, comp in obs_obj.components.items(): # dict in components and add them to the list
            fhir_data["component"].append({
                "code": {
                    "coding": [{"system": "http://loinc.org", "code": comp.code, "display": comp.display}]
                },
                "valueQuantity": {
                    "value": comp.value,
                    "unit": comp.unit,
                    "system": "http://unitsofmeasure.org",
                    "code": comp.unit
                }
            })
            
        return fhir_data
        