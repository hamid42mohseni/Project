import random


#  Create Usernaem By PhoneNumber
def CreatUserName(phone_number) -> str:
    username = phone_number[4:8] + "".join(
        random.choices("abcdefghijklomnpqursxyz", k=5)
    )

    return username
