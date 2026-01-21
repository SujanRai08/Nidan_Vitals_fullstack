from datetime import datetime
from app.models.component import ObservationComponent

class Observation:
    def __init__(self,observation_id,patient_id,effective_datetime):
        self.observation_id = observation_id
        self.patient_id = patient_id
        self.effective_datetime = effective_datetime
        self.components = []
        self.bmi = None
        self.bmi_category = None