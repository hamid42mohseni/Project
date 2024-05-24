import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from _db.models import User
from Tools.Extention import CreatUserName
from Tools import Exception
from cache.cachTools import SmsCode
from Jwt.jwt import JWTHandler


class CoreUser:

    def __init__(self, db_connection: AsyncSession) -> None:
        self.db_connection = db_connection

    async def Create(self, phone_number: str) -> User:

        username = CreatUserName(phone_number)

        CreateUser = User(
            username=username,
            phone_number=phone_number,
            is_superuser=False,
            is_active=True,
            is_staff=False,
            password=None,
        )

        async with self.db_connection as conn:
            conn.add(CreateUser)
            await conn.commit()

        return CreateUser

    async def SelectUser(self, phone_number: str):
        query = sa.select(User).where(User.phone_number == phone_number)
        async with self.db_connection as session:
            user = await session.scalar(query)
            if user is None:
                raise Exception.UserExeption
        return {"username": user.username, "phone_number": user.phone_number}

    async def CreateSmsAndCeckUser(self, phone_number: str):
        # code = "1212"
        query = sa.select(User).where(User.phone_number == phone_number)

        async with self.db_connection as session:
            user = session.scalar(query)
            if user is None:
                raise Exception.PhoneNumberInNotCorrect
            return Exception.SmsSended

    async def SendCode(self, phone_number: str) -> JWTHandler:
        return await SmsCode(phone_number)
