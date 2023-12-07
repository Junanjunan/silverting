from fastapi import FastAPI, Request, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from local_settings import *
from app.db.session import get_db
from app.db.models import ExampleTable


app = FastAPI()

@app.get("/")
async def index(request: Request, db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        print("Connected to the database successfully!")
    except OperationalError as e:
        print(f"Failed to connect to the database. Error: {e}")
    return {"hello": "world"}


@app.get("/db-test")
async def test_db(request: Request, db: Session = Depends(get_db)):
    # query = db.query(ExampleTable).filter(ExampleTable.is_active == True).first()
    query = db.query(ExampleTable).filter(ExampleTable.is_active == 1).first()
    return {'DB_ENGINE': DB_ENGINE, 'name': query.name, 'True': query.is_active}

@app.get("/db-insert")
async def insert_db(request: Request, db: Session = Depends(get_db)):
    row0 = ExampleTable(name='False_0', is_active=0)
    row1 = ExampleTable(name='False', is_active=False)
    row2 = ExampleTable(name='True_1', is_active=1)
    row3 = ExampleTable(name='True', is_active=True)
    row_list = [row0, row1, row2, row3]
    # for i in row_list:
    #     db.add(i)
    # db.commit()
    # db.close()
    return {'result':'success'}
