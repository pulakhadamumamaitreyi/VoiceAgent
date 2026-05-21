PATIENTS = {
    "patient-123": {
        "name": "Maitreyi",
        "preferred_language": "Tamil"
    }
}

async def get_patient(patient_id: str):
    return PATIENTS.get(patient_id)
