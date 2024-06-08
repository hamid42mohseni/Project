import random
import redis
from datetime import datetime, timedelta
from rest_framework.response import Response
from Tools.Exeptions import SmsSended, CodeErr
from Tools.JwtTokens import AccessTokenCustom


class RedisConnection:
    def __init__(self, host="localhost", port=6379, db=0):
        self._redis = redis.Redis(host=host, port=port, db=db)

    def __enter__(self):
        return self._redis

    def __aenter__(self):
        return self._redis

    def __exit__(self, xc_type, exc_value, traceback):
        self._redis.close()


# Send Sms For User
def SmsCode(phone_number: str):
    with RedisConnection() as rd:
        if rd.exists("exp"):
            raise SmsSended

        code = random.randint(1000, 9999)
        ExpTime = datetime.now() + timedelta(minutes=1)

        rd.set(name=phone_number, value=code)
        rd.set(name="exp", value=str(ExpTime))

        rd.expire("exp", 60)
        rd.expire(name=phone_number, time=60)
        return {"code": code, "exp": ExpTime}


def Check_code(ph, code):

    with RedisConnection() as Rd:
        Keycode = Rd.get(ph)

    if not Keycode:
        raise CodeErr

    Keycode = Keycode.decode("utf-8")

    if Keycode != code:
        raise CodeErr

    return AccessTokenCustom(ph)
