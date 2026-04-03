import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_db_and_tables(Base):
	Base.metadata.create_all(bind=engine)

load_dotenv()  # imports all the environment variables
sqlite_url = os.getenv('DATABASE_URL')  # defines the database and dialect object

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args,echo=True)  # lazy initialization of the engine

Session = sessionmaker(engine)  # factory (pattern) for Session class instances with engine as default