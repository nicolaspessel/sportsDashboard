import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def create_db_and_tables(Base):
        Base.metadata.create_all(bind=engine)

load_dotenv()  # imports all the environment variables
sqlite_url = os.getenv('DATABASE_URL')  # defines the database and dialect object

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True)  # lazy initialization of the engine

Base = declarative_base()

class Team(Base):  # inherits fom declarative base
    __tablename__ = "Team X"

    name: String = Column(String, primary_key=True, index=True)
    titles: Integer = Column(Integer, index=True)
    region: String = Column(String, index=True)

t = Team()
create_db_and_tables(t)