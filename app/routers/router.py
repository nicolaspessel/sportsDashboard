from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.schemas import TeamResponse
from ..services.service import get_team_by_id

def get_session():
	session = Session()
	try:
		yield session  # pause and returns the session value
	finally:
		session.close()  # once the session is finished, the session is closed

router = APIRouter()

@router.get("/teams/{team_id}", response_model=TeamResponse)
def get_team(team_id: int, session: Session = Depends(get_session)):
    team = get_team_by_id(team_id=team_id, session=session)

    if not team:
        raise HTTPException(status_code=404, detail="Item not found")  # terminates function and sends HTTP error

    return team