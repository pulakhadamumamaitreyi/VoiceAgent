from app.tools.scheduler import BOOKED

async def create_booking(patient_id, doctor, slot):

    if slot in BOOKED:
        return {
            "success": False,
            "message": "Slot already booked"
        }

    BOOKED.append(slot)

    return {
        "success": True,
        "doctor": doctor,
        "slot": slot
    }
