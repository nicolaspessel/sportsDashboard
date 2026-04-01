from abc import ABC, abstractmethod
from sqlalchemy import select, insert, delete
from sqlalchemy.orm import Session
from ..models.model import Team

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
        """Fetches a team by its primary key. The parameters within select are discarded after being
        used in the query, no need to store them in the instance with self."""
        
        return self.session.execute(
            select(Team).where(Team.id == team_id)  # SQLAlchemy finds model/table by __tablename__
        )

    def create_team(self, name: str, titles: int, region: str):
        self.session.execute(
            insert(Team),
            [
                {"name": name, "titles": titles, "region": region}
            ]
        )
        self.session.commit()

    def delete_team(self, team_id: int):
        self.session.execute(
            delete(Team).where(Team.id == team_id)
        )
        self.session.commit()  # saves pending changes to the database within the current transaction