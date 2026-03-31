import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.model import Team

def create_db_and_tables(Base):
	Base.metadata.create_all(bind=engine)


def get_db():
	db = Session()
	try:
		yield db  # pause and returns the session value
	finally:
		db.close()  # once the session is finished, the session is closed


load_dotenv()  # imports all the environment variables
sqlite_url = os.getenv('DATABASE_URL')  # defines the database and dialect object

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args,echo=True)  # lazy initialization of the engine

Session = sessionmaker(engine)  # factory (pattern) for Session instances with engine as default