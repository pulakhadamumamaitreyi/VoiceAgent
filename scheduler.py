from datetime import datetime
DOCTOR_SLOTS = {
    "Dr Priya": [
        "2026-05-22 17:00",
        "2026-05-22 18:00",
        "2026-05-22 19:00"
    ]
}

BOOKED = []

async def check_availability(doctor: str, date: str):

    available = []

    for slot in DOCTOR_SLOTS.get(doctor, []):

        if slot not in BOOKED:
            available.append(slot)

    return available
