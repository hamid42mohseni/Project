from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:ha1mi2d3@localhost/Mazer"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionnLocal = async_sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def get_db():
    db = SessionnLocal()
    try:
        yield db
    finally:
        await db.close()
