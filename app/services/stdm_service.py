from sqlalchemy.orm import Session
from repositories.stdm_repo import StadiumRepository
from repositories.team_repo import TeamRepository
from schemas.stdm_schema import StadiumUpdate
from exceptions import TeamNotFoundError

def create_new_stadium(name: str, location: str, team_id: int, session: Session):
    team = TeamRepository(session=session).get_team_by_id(team_id=team_id)
    if not team:
        raise TeamNotFoundError

    new_stadium = StadiumRepository(session=session)
    new_stadium.create_stadium(name=name, location=location, team_id=team_id)


def patch_stadium(stadium_id: int, stadium_update: StadiumUpdate, session: Session):
    stdm_to_updt = StadiumRepository(session=session)
    return stdm_to_updt.update_stadium(stadium_id=stadium_id, stadium_update=stadium_update)