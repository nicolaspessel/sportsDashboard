from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.model import Teams
from app.db.dbconfigs import create_db_and_tables
from app.routers.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    create_db_and_tables()
    yield
    # shutdown

app = FastAPI(lifespan=lifespan)

app.include_router(router)

@app.get("/")
async def root():
    return{
        "message": "Hello World!"
    }