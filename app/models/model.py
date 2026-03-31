from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # uses the declarative base object

class Team(Base):  # inherits fom declarative base
    __tablename__ = "Team X"

    id: Integer = Column(Integer, primary_key=True, autoincrement=True, index=True)  # surrogate key
    name: String = Column(String, index=True)
    titles: Integer = Column(Integer, index=True)
    region: String = Column(String, index=True)