from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:password@localhost/voice_ai"

engine = create_engine(DATABASE_URL)

class PatientMemory:

    async def get_patient_summary(self, patient_id: str):

        return """
        Preferred language: Tamil
        Usually books evening appointments
        Last appointment canceled
        """
