from sqlalchemy.orm import Session
from models.model import Teams
from repositories.athl_repo import AthleteRepository

def create_new_athlete(athl_id: int, full_name: str, position: str, age: int, weight: float, \
                       height: float, jersey_num: int, debut: int, team: Teams, session: Session):
    new_athlete = AthleteRepository(session=session)
    new_athlete.create_athlete(athl_id=athl_id, full_name=full_name, position=position, age=age, \
                               weight=weight, height=height, jersey_num=jersey_num, debut=debut, team=team)