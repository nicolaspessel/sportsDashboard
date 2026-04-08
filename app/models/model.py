from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # uses the declarative base object

class Teams(Base):  # inherits fom declarative base
    """The Mapped and mapped_column are the modern syntax for SQLAlchemy 2.0, allowing the use of python 
    native types and type hints, while Column is the legacy declaration for all SQLAlchemy systems and versions."""

    __tablename__ = "Teams"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  
    name: Mapped[str]  # class that represents an ORM mapped attribute in a class
    titles: Mapped[int]
    region: Mapped[str]