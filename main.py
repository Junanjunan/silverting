from fastapi import FastAPI, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import SessionLocal, create_tables, Item


async def get_db_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


app = FastAPI()


@app.get("/db-init")
async def startup_event():
    await create_tables()
    return {"status":"success"}

@app.get("/")
async def index(db: AsyncSession = Depends(get_db_session)):
    async with db.begin():
        result = await db.execute(select(Item))
        items = result.scalars().all()
    return items