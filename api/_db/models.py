from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import Mapped
from .engine import Base

from datetime import datetime


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str]
    phone_number: Mapped[str]
    is_superuser: Mapped[bool]
    password: Mapped[str]
    is_active: Mapped[bool]
    is_staff: Mapped[bool]
    last_seen = Column(DateTime, default=datetime.now)
    date_joined = Column(DateTime, default=datetime.now)
    