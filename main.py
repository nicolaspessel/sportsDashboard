from fastapi import FastAPI
from app.models.model import Team
from app.db.dbconfigs import create_db_and_tables

app = FastAPI()

t = Team()
create_db_and_tables()

@app.get("/")
async def root():
    return{
        "message": "Hello World!"
    }