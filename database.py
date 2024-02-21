from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool


DATABASE_URL = "mysql+pymysql://gnutest:86357811@localhost/silverting"

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=40,
    pool_timeout=60,
    pool_recycle=20,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=True,
)

Base = declarative_base()


class Item(Base):

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)


async def create_tables():
    with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)