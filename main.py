from fastapi import FastAPI, Request, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from local_settings import *
from app.db.session import get_db


app = FastAPI()

@app.get("/")
async def index(request: Request, db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        print("Connected to the database successfully!")
    except OperationalError as e:
        print(f"Failed to connect to the database. Error: {e}")
    return {"hello": "world"}