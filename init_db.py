from sqlalchemy import inspect

from app.db.session import engine, SessionLocal
from app.db.models import Base, ExampleTable
from app.core.config import settings


db = SessionLocal()

inspector = inspect(engine)
print(inspector.get_table_names())

"""
Have to keep order when creating table.
    1. Base = declarative_base()
    2. class ExampleTable(Base): - class for Table
    3. Base.metadata.create_all(bind=engine)
If 3 execute before 2, the table is not generated.
It is not error. Table is not generated but the reason is not error.
""" 
Base.metadata.create_all(bind=engine)

new_row = ExampleTable(name="Example", is_active=True)
db.add(new_row)
db.commit()
db.close()

print(f"Table was generated in {settings.CURRENT_DB_ENGINE}")