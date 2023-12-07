from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class ExampleTable(Base):
    __tablename__ = "example_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    is_active = Column(Boolean, default=False)