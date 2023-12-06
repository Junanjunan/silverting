from sqlalchemy import Column, Integer, String, Boolean, inspect
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from main import engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=True)
db = SessionLocal()

inspector = inspect(engine)
print(inspector.get_table_names())

########################################################################
"""
Have to keep order when creating table.
    1. Base = declarative_base()
    2. class ExampleTable(Base): - class for Table
    3. Base.metadata.create_all(bind=engine)
If 3 execute before 2, the table is not generated.
It is not error. Table is not generated but the reason is not error.
""" 
Base = declarative_base()

class ExampleTable(Base):
    __tablename__ = "example_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    is_active = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)
########################################################################

new_row = ExampleTable(name="Example", is_active=True)
db.add(new_row)
db.commit()
db.close()