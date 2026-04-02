from sqlalchemy.orm import Session
from ..repositories.repo import TeamRepository

def get_team_by_id(team_id: int, session: Session):
    team = TeamRepository(session=session)
    return team.get_team_by_id(team_id)

def create_team(name: str, titles: int, region:str, session: Session):
    new_team = TeamRepository(session=session)
    new_team.create_team(name=name, titles=titles, region=region)

def delete_team(team_id: int, session: Session):
    team_to_del = TeamRepository(session=session)
    team_to_del.delete_team(team_id=team_id)