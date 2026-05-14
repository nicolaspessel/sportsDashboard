from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Table, Column

class Base(DeclarativeBase):  # base for all ORM tables/models 
    pass


association_table = Table(
    "association_table",
    Base.metadata,
    Column("team_id", ForeignKey("Teams.id"), primary_key=True),
    Column("player_id", ForeignKey("Athletes.id"), primary_key=True),
)


class Teams(Base):  # class that represents an ORM mapped attribute in a class
    """The Mapped and mapped_column are the modern syntax for SQLAlchemy 2.0, allowing the use of python 
    native types and type hints, while Column is the legacy declaration for all SQLAlchemy systems and versions."""

    __tablename__ = "Teams"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    espn_id: Mapped[int]
    name: Mapped[str]  
    abbreviation: Mapped[str]
    is_active: Mapped[bool]
    titles: Mapped[int]
    region: Mapped[str]
    stadium: Mapped["Stadiums"] = relationship(back_populates="team", uselist=False)  # allows directly acess to Stadium without a JOIN
    athletes: Mapped[list["Athletes"]] = relationship(back_populates="teams", 
        secondary=association_table)

    
class Stadiums(Base):
    __tablename__ = "Stadiums"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("Teams.id"))  # Stadium that belongs to the Team X
    name: Mapped[str] 
    location: Mapped[str]
    team: Mapped["Teams"] = relationship(back_populates="stadium", single_parent=True)  # one-to-one on Child.parent side


class Athletes(Base):
    __tablename__ = "Athletes"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    position: Mapped[str]
    age: Mapped[int]
    weight: Mapped[int]
    height: Mapped[int]
    jersey_num: Mapped[int]
    debut: Mapped[int | None]
    teams: Mapped[list["Teams"]] = relationship(back_populates="athletes", 
        secondary=association_table)