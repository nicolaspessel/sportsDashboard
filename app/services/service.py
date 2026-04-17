from sqlalchemy.orm import Session
from ..repositories.repo import TeamRepository
from ..schemas.schemas import TeamUpdate

def get_team_by_id(team_id: int, session: Session):
    team = TeamRepository(session=session)
    return team.get_team_by_id(team_id=team_id)

def get_all_teams(session: Session):
    teams = TeamRepository(session=session)
    return teams.get_teams()

def patch_team(team_id: int, team_update: TeamUpdate, session: Session):
    team_to_updt = TeamRepository(session=session)
    return team_to_updt.update_team(team_id=team_id, team_update=team_update)

def create_new_team(name: str, titles: int, region:str, session: Session):
    new_team = TeamRepository(session=session)
    new_team.create_team(name=name, titles=titles, region=region)

def remove_item(team_id: int, session: Session):
    team_to_del = TeamRepository(session=session)
    team_to_del.delete_team(team_id=team_id)