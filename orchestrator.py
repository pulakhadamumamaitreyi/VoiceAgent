from app.memory.redis_memory import SessionMemory
from app.memory.postgres_memory import PatientMemory
from app.tools.scheduler import check_availability
from app.tools.booking import create_booking
from app.voice.language import detect_language
from openai import AsyncOpenAI

client = AsyncOpenAI()

session_memory = SessionMemory()
patient_memory = PatientMemory()

SYSTEM_PROMPT = """
You are a multilingual healthcare appointment assistant.
You help users book, reschedule, and cancel appointments.
Always respond in the user's preferred language.
"""

async def handle_user_message(session_id: str, transcript: str):

    language = detect_language(transcript)

    session = await session_memory.get_session(session_id)

    patient_context = await patient_memory.get_patient_summary(
        patient_id="patient-123"
    )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "system",
            "content": f"Patient Context: {patient_context}"
        },
        {
            "role": "user",
            "content": transcript
        }
    ]

    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.2
    )

    text = response.choices[0].message.content

    if "appointment" in transcript.lower():

        slots = await check_availability(
            doctor="Dr Priya",
            date="2026-05-22"
        )

        if slots:
            booking = await create_booking(
                patient_id="patient-123",
                doctor="Dr Priya",
                slot=slots[0]
    }
