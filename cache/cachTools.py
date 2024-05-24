from datetime import datetime, timedelta
import random
import redis


class RedisConnection:
    def __init__(self, host="localhost", port=6379, db=0):
        self._redis = redis.Redis(host=host, port=port, db=db)

    def __enter__(self):
        return self._redis

    def __exit__(self, xc_type, exc_value, traceback):
        self._redis.close()


async def SmsCode(phone_number: str):
    with RedisConnection() as rd:
        if rd.exists("exp"):
            return {"detail": "Sended"}
        code = random.randint(1, 9999)
        ExpTime = datetime.now() + timedelta(minutes=2)

        rd.set("code", code)
        rd.set("exp", str(ExpTime))
        rd.expire("exp", 120)
        return {"code": code, "exp": ExpTime}
