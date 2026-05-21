from celery import Celery

celery = Celery(
    "campaigns",
    broker="redis://localhost:6379/0"
)

@celery.task
async def reminder_call(patient_id):

    print(f"Calling patient {patient_id}")
