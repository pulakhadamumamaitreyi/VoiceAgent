import redis
import json

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

class SessionMemory:

    async def get_session(self, session_id: str):
        data = r.get(session_id)

        if not data:
            return {}

        return json.loads(data)

    async def save_message(self, session_id, user, assistant):

        payload = {
            "user": user,
            "assistant": assistant
        }

        r.setex(
            session_id,
            1800,
            json.dumps(payload)
        )
