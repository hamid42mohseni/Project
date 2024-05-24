from fastapi import Body, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from _db.engine import get_db
import sys

sys.path.append("..")
# from core.UserBases import CoreUser
from _db.core.UserBases import CoreUser
from schema.CreateModels import UserCreate


router = APIRouter()


@router.post("/Create")
async def RegisterUser(
    db_connection: Annotated[AsyncSession, Depends(get_db)],
    data: UserCreate = Body(),
):
    user = await CoreUser(db_connection).Create(data.phone_number)
    return user


@router.get("/Select/{phone_number}/")
async def SelectUser(
    db_connection: Annotated[AsyncSession, Depends(get_db)], phone_number: str
):
    user = await CoreUser(db_connection).SelectUser(phone_number)
    return user


@router.get("/SendSms/{phone_number}")
async def SendCode(
    db_connection: Annotated[AsyncSession, Depends(get_db)],
    phone_number: str,
):
    response = await CoreUser(db_connection).SendCode(phone_number)
    return response
