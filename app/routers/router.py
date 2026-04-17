from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.dbconfigs import get_session
from ..schemas.schemas import TeamResponse, TeamCreate, TeamUpdate
from ..services.service import get_team_by_id, get_all_teams, create_new_team, remove_item, patch_team

router = APIRouter()

@router.get("/teams/{team_id}", response_model=TeamResponse)
def get_team(team_id: int, session: Session = Depends(get_session)):
    team = get_team_by_id(team_id=team_id, session=session)

    if not team:
        raise HTTPException(status_code=404, detail="Item not found")  # terminates function and sends HTTP error

    return team

@router.get("/teams/", response_model=list[TeamResponse])
def get_teams(session: Session = Depends(get_session)):
    teams = get_all_teams(session=session)

    if not teams:
        raise HTTPException(status_code=404, detail="Item not found")

    return teams

@router.patch("/teams/{team_id}", response_model=TeamResponse)
def update_team(team_id: int, team_update: TeamUpdate, session: Session = Depends(get_session)):
    team = patch_team(team_id=team_id, team_update=team_update, session=session)

    if not team:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return team

@router.post("/teams/", status_code=201)
def create_team(team: TeamCreate, session: Session = Depends(get_session)):
    team = create_new_team(name=team.name, titles=team.titles, region=team.region, session=session)
    
@router.delete("/teams/{team_id}", status_code=204)
def delete_team(team_id: int, session: Session = Depends(get_session)):
    remove_item(team_id=team_id, session=session)