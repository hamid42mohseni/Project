from fastapi import Body, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from _db.engine import get_db
from core.UserBases import CoreUser
import sys

sys.path.append("..")
from schema.CreateModels import UserCreate


router = APIRouter()


@router.post("/Create")
async def RegisterUser(
    db_connection: Annotated[AsyncSession, Depends(get_db)],
    data: UserCreate = Body(),
):
    user = await CoreUser(db_connection).Create(data.phone_number)
    return user


@router.get("/get")
async def getuser(
    db_connection: Annotated[AsyncSession, Depends(get_db)], phone_number: str
):
    user = await CoreUser(db_connection).get(phone_number)
    return user


@router.get("/login")
async def Login(
    db_connection: Annotated[AsyncSession, Depends(get_db)],
    phone_number: str,
    code: str,
):
    response = await CoreUser(db_connection).Login(code, phone_number)
    return response
