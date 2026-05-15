from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.dbconfigs import get_session
from ..schemas.athl_schema import AthleteResponse
from ..services.athl_service import get_team_athletes
from ..exceptions import TeamNotFoundError

athl_router = APIRouter()

@athl_router.get("/{team_id}/players", response_model=list[AthleteResponse])
def get_team_players(team_id: int, session: Session = Depends(get_session)):
    try:
        players = get_team_athletes(team_id=team_id, session=session)
    except TeamNotFoundError:
        raise HTTPException(status_code=404, detail="Team not found")
    
    return players