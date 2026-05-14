from sqlalchemy.orm import Session
from ..models.model import Athletes, Teams

class AthleteRepository():
    def __init__(self, session: Session):
        self.session = session

    def create_athlete(self, athl_id: int, full_name: str, position: str, age: int, weight: \
                       float, height: float, jersey_num: int, debut: int, team: Teams):
        new_athlete = Athletes(id=athl_id, full_name=full_name, position=position, age=age, \
                               weight=weight, height=height, jersey_num=jersey_num, debut=debut)
        
        team.athletes.append(new_athlete)
        self.session.add(new_athlete)
        self.session.commit()