from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# A model is a Python class that represents a table in a database.
# Each attribute within the class is a column of the table.

Base = declarative_base()  # uses the declarative base object

class Team(Base):  # inherits fom declarative base
    __tablename__ = "Team X"

    name: String = Column(String, primary_key=True, index=True)
    titles: Integer = Column(Integer, index=True)
    region: String = Column(String, index=True)