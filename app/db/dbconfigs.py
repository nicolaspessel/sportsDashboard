import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.model import Base

load_dotenv()  # imports all the environment variables
sqlite_url = os.getenv('DATABASE_URL')  # defines the database and dialect object

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args,echo=True)  # lazy initialization of the engine

# factory for Session class object with engine as defaut
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  

def create_db_and_tables():
	Base.metadata.create_all(bind=engine)

def get_session():
	session = SessionLocal()  # when calling the factory, a Session object is returned
	try:
		yield session  # pause and returns the session value
	finally:
		session.close()  # once the session is finished, the session is closed