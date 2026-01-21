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
    def get_risk_status(bmi,systolic, distolic):
        """
        Requirement: Red Alerts if BMI >= 30 or BP >= 140/90.
        Returns: 'High Risk', 'Warning', or 'Normal'
        """
        if bmi >= 30 or systolic >= 140 or distolic >= 90:
            return "High Risk"  # Red
        elif 25 <= bmi < 30:
            return "Warning"    # Orange
        return "Normal" # Green
    
    
    
