from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.dbconfigs import create_db_and_tables
from app.routers.team_router import team_router
from app.routers.stdm_router import stdm_router
from app.routers.athl_router import athl_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    create_db_and_tables()
    yield
    # shutdown

app = FastAPI(lifespan=lifespan)

app.include_router(prefix="/teams", router=team_router, tags=["teams"])
app.include_router(prefix="/stadiums", router=stdm_router, tags=["stadiums"])
app.include_router(prefix="/teams", router=athl_router, tags=["players"])

@app.get("/")
async def root():
    return{
        "message": "Hello World!"
    }