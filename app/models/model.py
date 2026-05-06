from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):  # base for all ORM tables/models 
    pass

class Teams(Base):  # class that represents an ORM mapped attribute in a class
    """The Mapped and mapped_column are the modern syntax for SQLAlchemy 2.0, allowing the use of python 
    native types and type hints, while Column is the legacy declaration for all SQLAlchemy systems and versions."""

    __tablename__ = "Teams"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
    name: Mapped[str]  
    abbreviation: Mapped[str]
    is_active: Mapped[bool]
    titles: Mapped[int]
    region: Mapped[str]
    children: Mapped["Stadiums"] = relationship(back_populates="parent", uselist=False)  # allows directly acess to Stadium without a JOIN

    
class Stadiums(Base):
    __tablename__ = "Stadiums"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("Teams.id"))  # Stadium that belongs to the Team X
    name: Mapped[str] 
    location: Mapped[str]
    parent: Mapped["Teams"] = relationship(back_populates="children", single_parent=True)  # one-to-one on Child.parent side