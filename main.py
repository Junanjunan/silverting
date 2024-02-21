from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal, create_tables, Item


async def get_db_session():
    with SessionLocal() as session:
        yield session


app = FastAPI()


@app.get("/db-init")
async def startup_event():
    await create_tables()
    return {"status":"success"}

@app.get("/")
async def index(db: Session = Depends(get_db_session)):
    with db.begin():
        result = db.execute(select(Item))
        items = result.scalars().all()
    return items