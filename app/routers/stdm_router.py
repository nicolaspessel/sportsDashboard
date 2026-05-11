from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.stdm_schema import StadiumResponse, StadiumCreate, StadiumUpdate
from services.stdm_service import create_new_stadium, patch_stadium
from db.dbconfigs import get_session
from exceptions import TeamNotFoundError

stdm_router = APIRouter()

@stdm_router.patch("/{stdm_id}", response_model=StadiumResponse)
def update_stadium(stdm_id: int, stdm_update: StadiumUpdate, session: Session = Depends(get_session)):
    stadium = patch_stadium(stadium_id=stdm_id, stadium_update=stdm_update, session=session)

    if not stadium:
        raise HTTPException(status_code=404, detail="Item not found")

    return stadium


@stdm_router.post("/", status_code=201)
def create_stadium(stadium: StadiumCreate, session: Session = Depends(get_session)):
    try:
        stadium = create_new_stadium(name=stadium.name, location=stadium.location, team_id=stadium.team_id, session=session)
    except TeamNotFoundError:
        raise HTTPException(status_code=404, detail="Team not found")
