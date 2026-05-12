from sqlalchemy.orm import Session
from models.model import Stadiums
from schemas.stdm_schema import StadiumUpdate

class StadiumRepository():
    def __init__(self, session: Session):
        self.session = session

    def update_stadium(self, stadium_id: int, stadium_update: StadiumUpdate):
        stadium_obj = self.session.get(Stadiums, stadium_id)

        if(stadium_obj):
            for field in stadium_update.model_fields_set:
                setattr(stadium_obj, field, getattr(stadium_update, field))
            self.session.commit()

        return stadium_obj

    def create_stadium(self, name: str, location: str, team_id: int):
        new_stadium = Stadiums(name=name, location=location, team_id=team_id)  # needs the foreign key
        self.session.add(new_stadium)
        self.session.commit()