from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from ..models.model import Teams
from ..schemas.schemas import TeamUpdate

class BaseRepository(ABC):  # creates an abstract class the inherits from ABC and have abstract methods
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod  # implements an abstract method without body that will be implemented in child classes
    def get_team_by_id(self, team_id: int):
        pass

    @abstractmethod
    def create_team(self, name: str, titles: int, region: str):
        pass

    @abstractmethod
    def delete_team(self, team_id: int):
        pass


class TeamRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session)  # stores self.session = session

    def get_team_by_id(self, team_id: int):  
        """Fetches a team by its primary key. We used a Session.get() as we're working with a 
        ORM approach within the whole project. The core alternative is also below."""
        
        return self.session.get(Teams, team_id)
        # Core alternative: .execute(select(Team).where(Team.id == team_id)) - SQLAlchemy finds model/table by __tablename__

    def update_team(self, team_id: int, team_update: TeamUpdate):
        team_obj = self.session.get(Teams, team_id)  # fetches the existing team in the database

        if(team_obj):
            for field in team_update.model_fields_set:
                setattr(team_obj, field, getattr(team_update, field))  # update the db w/ the new update_team fields
            self.session.commit()

        return team_obj

    def create_team(self, name: str, titles: int, region: str):
        new_team = Teams(name=name, titles=titles, region=region)
        self.session.add(new_team)
        self.session.commit()  # saves pending changes to the database within the current transaction

    def delete_team(self, team_id: int):
        team_to_del = self.session.get(Teams, team_id)  # fetches the team
        self.session.delete(team_to_del)
        self.session.commit()  