import jwt
from datetime import timedelta, datetime
import sys

sys.path.append("..")
from schema.CreateModels import JWTRespons, JWTResponsePaylad
from typing import Annotated
from fastapi import Header, status
from fastapi.exceptions import HTTPException
from Backend.Backend import Local_setting


class JWTHandler:
    @staticmethod
    def Generate(
        phone_number: str, ExpTimeStamp: int | None = None
    ) -> JWTResponsePaylad:
        ExpTime = Local_setting.ACCESS_TOKEN_EXP_MINUTE
        SecretKey = Local_setting.SecretKey
        ExpDelta = datetime.now() + timedelta(minutes=ExpTime)

        Encode = {
            "exp": ExpTimeStamp if ExpTimeStamp else ExpDelta,
            "phone_number": phone_number,
        }

        EncodeJWT = jwt.encode(
            Encode,
            SecretKey,
            algorithm=Local_setting.ALGORITM,
        )
        return JWTResponsePaylad(Access=EncodeJWT)

    @staticmethod
    def Verify(AuthToken: Annotated[str, Header()]):
        JWT_token = AuthToken
        if not JWT_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Auth Header Not Found !!",
            )

        try:
            toke_data = jwt.decode(
                JWT_token,
                Local_setting.SecretKey,
                algorithms=Local_setting.ALGORITM,
            )

            if datetime.fromtimestamp(toke_data["exp"] < datetime.now()):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token Expiered",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except jwt.exceptions.PyJWTError:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could Not Validate :D",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return JWTRespons(**toke_data)
