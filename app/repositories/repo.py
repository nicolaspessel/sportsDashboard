from abc import ABC, abstractmethod
from sqlalchemy import select, insert, delete
from sqlalchemy.orm import Session
from ..models.model import Team

class BaseRepository(ABC):
    def __init__(self, db: Session):
        pass

    @abstractmethod
    def get_team_by_id(self, db: Session, team_id: int):
        pass

    @abstractmethod
    def create_team(self, db: Session, team: TeamCreate):
        pass

    @abstractmethod
    def delete_team(self, db: Session, team_id: int):
        pass


class TeamRepository(BaseRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_team_by_id(self, team_id: int):
        self.team_id = team_id

        return self.db.execute(
            select(self.db).where(self.db.id == self.team_id)
        )

    def create_team(self, team: int, name: str, titles: int, region: str):
        self.team = team
        self.name = name
        self.titles = titles
        self.region = region

        self.db.execute(
            insert(Team),
            [
                {"name": self.name, "titles": self.titles, "region": self.region}
            ]
        )

    def delete_team(self, team_id: int):
        self.team_id = team_id

        self.db.execute(
            delete(self.db).where(self.db.id == self.team_id)
        )