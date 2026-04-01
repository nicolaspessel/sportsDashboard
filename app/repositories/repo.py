from abc import ABC, abstractmethod
from sqlalchemy import select, insert, delete
from sqlalchemy.orm import Session
from ..models.model import Team
from ..schemas.schemas import TeamCreate, TeamResponse

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
        
        return self.session.get(Team, team_id)
        # Core alternative: .execute(select(Team).where(Team.id == team_id)) - SQLAlchemy finds model/table by __tablename__

    def create_team(self, name: str, titles: int, region: str):
        new_team = Team(name=name, titles=titles, region=region)
        self.session.add(new_team)
        self.session.commit()  # saves pending changes to the database within the current transaction

    def delete_team(self, team_id: int):
        team_to_del = self.session.get(Team, team_id)
        self.session.delete(Team, team_to_del)
        self.session.commit()  