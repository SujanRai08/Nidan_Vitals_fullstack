from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
from app.models.observation import Observation
from app.models.component import ObservationComponent
from app.services.observation_service import ObservationService
from app.storage.db import db

router = APIRouter()

@router.post("/api/fhir/observation")
def create_observation(payload):
    # validation
    if payload.get("resourceType") != "Observation":
        raise HTTPException(status_code=400, detail="Invalid FHIR resources")
    
    # create the observation object. using uuid to ensure unique id

    obs_id = str(uuid.uuid4())
    patient_ref = payload.get("subject", {}).get("reference", "Unknown")
    obs = Observation(
        observation_id="OBS-" + datetime.utcnow().isoformat(),
        patient_id=payload["subject"]["reference"],
        effective_datetime=datetime.utcnow()
    )
    height = None
    weight = None
    systolic = 0
    diastolic = 0

    for comp in payload.get("component",[]):
        code = comp["code"]["coding"][0]["code"]
        display = comp["code"]["coding"][0]["display"]
        value = comp["valueQuantity"]["value"]
        unit = comp["valueQuantity"]["unit"]

        # component object
        new_comp = ObservationComponent(code,display,value,unit)

        obs.components[code] = new_comp # store in dict using the code as they key

        # values for BMI and Risk calculation
        if code == "8302-2": # Height
            height = value
        elif code == "29463-7": # Weight
            weight = value
        elif code == "8480-6": # Systolic
            systolic = value
        elif code == "8462-4": # Diastolic
            diastolic = value

    if height and weight:
        bmi_value = ObservationService.calculate_bmi(weight,height)
        obs.bmi = bmi_value
        obs.bmi_category = ObservationService.bmi_category(bmi_value)

        # add risk status
        obs.risk_status = ObservationService.get_risk_status(bmi_value,systolic, diastolic)

    # saving to inmemory db
    db.save(obs)

    # return response
    return {
        "status": "success",
        "observation_id": obs.observation_id,
        "bmi": obs.bmi,
        "category": obs.bmi_category,
        "risk": getattr(obs, 'risk_status', 'Normal')
    }


